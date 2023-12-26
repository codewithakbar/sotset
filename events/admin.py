from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date')
    list_filter = ('location', 'date')
    search_fields = ('title',)

admin.site.register(Event, EventAdmin)
