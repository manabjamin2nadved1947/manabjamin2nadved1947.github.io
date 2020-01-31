from django.contrib import admin

# Register your models here.
from csfest.models import Event, Participant, Moderator

admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Moderator)


