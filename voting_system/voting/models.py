from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Voter(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length= 25 )

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=255)
    bio= models.TextField()
    photo= models.ImageField(upload_to='candidates/')

class Election(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)

