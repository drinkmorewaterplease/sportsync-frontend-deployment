from django.contrib import admin
from .models import Event, EventParticipant

# Register your models here.
admin.site.register(Event)
admin.site.register(EventParticipant)
