from django.db import models

from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse

class Event(models.Model):
	name = models.CharField(max_length=200, help_text='Enter an event name (e.g. Coding round, Seminar etc)')
	description = models.TextField(max_length=1000)
	
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('event-detail', args=[str(self.id)])


class Participant(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	college=models.CharField(max_length=500)
	email=models.EmailField()
	events_participate=models.ManyToManyField(Event, help_text='Select  events you participate')
	user=models.OneToOneField(User,on_delete=models.CASCADE)

	class Meta:
		ordering = ['last_name', 'first_name','college']


	def __str__(self):
        
		return f'{self.last_name}, {self.first_name}, {self.college}'
    
	def get_absolute_url(self):
        
		return reverse('participant-detail', args=[str(self.id)])
        
	def display_events_participate(self):
       

		return ', '.join(events_participate.name for events_participate in self.events_participate.all()[:3])
    
	display_events_participate.short_description = 'Events'



class Moderator(models.Model):
	mods_name=models.CharField(max_length=200)
	mods_email=models.EmailField(blank=True)
	#username=models.OneToOneField(User,max_length=200,blank=False,on_delete=models.SET_NULL,null=True)


	def __str__(self):
        
		return self.mods_name
