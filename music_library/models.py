from django.db import models

# Create your models here.

class Music_Library(models.Modle):
    title = models.CharField(max_length = 225)
    artist = models.CharField(max_length = 225)
    album = models.CharField(max_length = 225)
    release_date = models.DateField()
    genre = models.CharField(max_length = 225)