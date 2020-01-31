from django import forms
from django.forms import ModelForm
from csfest.models import Participant
from csfest.models import Event
from django.forms.widgets import CheckboxSelectMultiple

class ParticipantCreateForm(ModelForm):
	events_participate = forms.ModelMultipleChoiceField( widget = forms.CheckboxSelectMultiple,queryset = Event.objects.all(),required = True)

	class Meta:
		model = Participant
		fields = ('first_name', 'last_name', 'college', 'email', 'events_participate')
	#def __init__(self, *args, **kwargs):

		#super(ParticipantCreateForm,self).__init__(*args, **kwargs)

		#self.fields['events_participate'].widget = CheckboxSelectMultiple()
		#self.fields['events_participate'].queryset = Event.objects.all() 

	def save(self, user=None):
		user_profile = super(ParticipantCreateForm, self).save(commit=False)
		if user:
			user_profile.user = user
		user_profile.save()
		return user_profile

class ParticipantUpdateForm(ModelForm):
	events_participate = forms.ModelMultipleChoiceField( widget = forms.CheckboxSelectMultiple,queryset = Event.objects.all(),required = True)

	class Meta:
		model = Participant
		fields = ('first_name', 'last_name', 'college', 'email', 'events_participate')


