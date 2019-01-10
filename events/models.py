from django.db import models

class Event(models.Model):
    api_url = models.CharField(max_length=255)
    
