from django.db import models

# Create your models here.
class save(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
