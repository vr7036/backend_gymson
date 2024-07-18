from django.db import models

class Gym(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    rating=models.IntegerField(null=True)


