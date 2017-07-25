from django.db import models
import datetime

# Create your models here.
class Course(models.Model):
    titles = models.CharField(max_length = 20)
    location = models.CharField(max_length = 30)
    trainer = models.CharField(max_length = 10)
