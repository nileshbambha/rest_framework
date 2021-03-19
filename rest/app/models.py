from django.db import models

class student(models.Model):
    rno = models.IntegerField()
    name = models.CharField(max_length=50)  
    std = models.CharField(max_length=50)
    