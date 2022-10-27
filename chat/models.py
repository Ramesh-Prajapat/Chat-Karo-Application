from django.db import models

# Create your models here.


class UserData(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='', unique=True)
    gender = models.CharField(max_length=6)
    state = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default='')


class Room(models.Model):
    name = models.CharField(max_length=20)


class Chat(models.Model):
    objects = None
    uid = models.IntegerField()
    chat = models.CharField(max_length=5000)
    roomid = models.IntegerField()
