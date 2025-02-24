#!/ismailmwarumba/bin/env python
from django.db import models

class AboutUs(models.Model):
    motto = models.CharField(max_length=255)
    mission = models.TextField()
    vision = models.TextField()

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()

class NewsEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

class Admission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()