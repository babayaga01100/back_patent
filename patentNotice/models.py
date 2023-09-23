from django.db import models

# Create your models here.

class PatentNotice(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.TextField()
    date = models.DateField()