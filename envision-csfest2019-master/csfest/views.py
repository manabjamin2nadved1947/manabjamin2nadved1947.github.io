from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy 
# Create your views here.
from csfest.models import Event, Participant, Moderator

def index(request):
	#count no.of events (for checking purpose)
	num_events = Event.objects.count()
	num_participants = Participant.objects.count()
	context = {
		'num_events':  num_events,
		'num_participants': num_participants,
	}
	return render(request, 'index.html',context)
def contacts(request):
	pass
	return render(request,'contacts.html')
def workforce(request):
	pass
	return render(request,'workforce.html')
def reach(request):
	pass
	return render(request,'reach.html')

from django.views import generic

class EventListView(generic.ListView):
	model = Event
	paginate_by = 10
	template_name = 'event_list.html' 

class EventDetailView(generic.DetailView):
	model = Event
	paginate_by = 10
	template_name = 'event_detail.html'
class ParticipantListView(generic.ListView):
	model = Participant
	paginate_by = 10
	template_name = 'participant_list.html'
class ParticipantDetailView(generic.DetailView):
	model = Participant
	paginate_by =10
	template_name = 'participant_detail.html'



def register(request):
	if request.method == 'POST':
		f = UserCreationForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request, 'Account created successfully, Login in your account to join events')
			return HttpResponseRedirect(reverse('register'))
 
	else:
		f = UserCreationForm()
 
	return render(request, 'register.html', {'form': f})

class ProfileDetailView(LoginRequiredMixin,generic.DetailView):
	model = Participant
	template_name = 'profile.html'
	
	def get_queryset(self):
		return Participant.objects.filter(user=self.request.user)
			

from csfest.forms import ParticipantCreateForm
from csfest.forms import ParticipantUpdateForm
from django.views.generic import FormView

class ParticipantCreate(FormView):
	form_class = ParticipantCreateForm
	template_name = 'csfest/participant_form.html'
	

	def form_valid(self, form):
		form.save(self.request.user)
		return super(ParticipantCreate, self).form_valid(form)
	success_url = reverse_lazy('index')
	 
class ParticipantUpdate(UpdateView):
	model = Participant
	form_class = ParticipantUpdateForm
	#fields = '__all__'
	#fields = ['first_name', 'last_name', 'college', 'email', 'events_participate']
	#exclude = ['username']
class ParticipantDelete(DeleteView):
	model = Participant
	success_url = reverse_lazy('index')
