from django.db import models

# Create your models here.
class Advisor(models.Model): 
    name = models.CharField(max_length=200)
    photo_url = models.URLField()
   

