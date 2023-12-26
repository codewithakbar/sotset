from django.contrib import admin
from .models import ChatMessage

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'sender', 'message', 'timestamp')
    search_fields = ('room_name', 'sender', 'message')
    list_filter = ('room_name', 'timestamp')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)

admin.site.register(ChatMessage, ChatMessageAdmin)
