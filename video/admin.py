from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader_name', 'upload_date', 'views')
    search_fields = ('title', 'uploader_name')
    list_filter = ('upload_date',)
    date_hierarchy = 'upload_date'
    ordering = ('-upload_date',)

admin.site.register(Video, VideoAdmin)
