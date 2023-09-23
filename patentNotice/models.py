from django.db import models

# Create your models here.

class PatentNotice(models.Model):
    title = models.TextField()
    image = models.TextField()
    image_url = models.TextField()
    date = models.TextField()