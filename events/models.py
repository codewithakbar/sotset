from django.db import models

class Event(models.Model):
    location_choices = [
        ('my_location', 'My Location'),
        ('online', 'Online'),
    ]

    date_choices = [
        (1, 'Today'),
        (2, 'Tomorrow'),
        (3, 'This week'),
        (4, 'This weekend'),
        (5, 'Next week'),
    ]

    title = models.CharField(max_length=255)
    location = models.CharField(max_length=20, choices=location_choices, default='my_location')
    date = models.IntegerField(choices=date_choices)
    
    def __str__(self):
        return self.title
