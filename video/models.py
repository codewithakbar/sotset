from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    thumbnail_url = models.URLField()
    video_url = models.URLField()
    duration = models.CharField(max_length=10)
    uploader_name = models.CharField(max_length=255)
    upload_date = models.DateTimeField()
    views = models.IntegerField()

    def __str__(self):
        return self.title
