from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sandik = models.IntegerField(default=0)  # sandik aidat
    dernek = models.IntegerField(default=0)  # dernek aidat
    address = models.CharField(max_length=200,default="")
    tel = models.CharField(max_length=15,default="")
    start_date = models.DateTimeField(default=datetime.datetime.utcnow())

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Dues_Sandik(models.Model):
    record_id = models.AutoField(primary_key=True)
    tc =  models.CharField(max_length=12)
    value = models.IntegerField(default=0) # sandik aidat
    insert_date = models.DateTimeField()


class Dues_Dernek(models.Model):
    record_id = models.AutoField(primary_key=True)
    tc =  models.CharField(max_length=12)
    value = models.IntegerField(default=0) # dernek aidat
    insert_date = models.DateTimeField()


class Credit(models.Model):
    record_id = models.AutoField(primary_key=True)
    tc =  models.CharField(max_length=12)
    value = models.IntegerField(default=0) # sandik aidat
    insert_date = models.DateTimeField()



class Outcome(models.Model):
    record_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    info =  models.CharField(max_length=200)
    value = models.IntegerField(default=0) # sandik aidat
    insert_date = models.DateTimeField()


