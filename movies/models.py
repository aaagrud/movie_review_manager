from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    title = models.CharField(max_length=250)
    year = models.TextField(max_length=5)
    summary = models.TextField(max_length=500)

class Director(models.Model):
    name = models.CharField(max_length=300)