from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    data = models.CharField(max_length=200)	
    date = models.DateTimeField('date published')
    location = models.CharField(max_length=200)
    image = models.ImageField('img', upload_to='img',null=True, blank=True)
    #image = models.CharField(max_length=200)
    #is_liked = models.CharField(max_length=200)
    is_liked = models.BooleanField(default=False)
