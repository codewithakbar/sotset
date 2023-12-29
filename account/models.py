from django.db import models
from django.conf import settings

from users.models import User
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return f'Profile of {self.user.username}'
    
