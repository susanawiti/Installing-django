from django.db import models

# Create your models here.
class student(models.Model):
    names = models.TextField()
    course = models.CharField(max_length = 200)
    year = models.IntegerField()