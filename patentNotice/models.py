from django.db import models

# Create your models here.

class PatentNoticeDate(models.Model):
    title = models.TextField()
    # date = models.DateField()
    
class PatentNotice(models.Model):
    title = models.ForeignKey('PatentNoticeDate', on_delete=models.CASCADE)
    image = models.TextField()
    image_url = models.TextField()