
from django.db import models

class Group(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='group_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
