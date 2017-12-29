from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils import timezone

DEFAULT_TC ="00000000000"
class Profile(models.Model):
    class Meta:
        verbose_name = 'Uyeler'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tc = models.CharField(max_length=11,default=DEFAULT_TC,db_index=True)
    ad = models.CharField(max_length=50,default="")
    soyad = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50, default="")
    sandik = models.IntegerField(default=0)  # sandik aidat
    dernek = models.IntegerField(default=0)  # dernek aidat
    address = models.CharField(max_length=200, default="")
    tel = models.CharField(max_length=15, default="")
    start_date = models.DateTimeField(default=timezone.now())

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
    class Meta:
        verbose_name = 'Sandik aidat'
    record_id = models.AutoField(primary_key=True)
    tc = models.CharField(max_length=12,db_index=True)
    value = models.IntegerField(default=0)  # sandik aidat
    insert_date = models.DateTimeField()

    def __str__(self):
        return "tc: " + str(self.tc) + " miktar: " + str(self.value) + " tarih : " + str(self.insert_date)





class Dues_Dernek(models.Model):
    class Meta:
        verbose_name = 'Dernek aidat'
    record_id = models.AutoField(primary_key=True)
    tc = models.CharField(max_length=12,db_index=True)
    value = models.IntegerField(default=0)  # dernek aidat
    insert_date = models.DateTimeField()

    def __str__(self):
        return "tc: " + str(self.tc) + " miktar: " + str(self.value) + " tarih : " + str(self.insert_date)


class Credit_Pays(models.Model):
    class Meta:
        verbose_name = 'Kredi ödenen'
    record_id = models.AutoField(primary_key=True)
    tc = models.CharField(max_length=12,db_index=True)
    value = models.IntegerField(default=0)  # sandik aidat
    insert_date = models.DateTimeField()

    def __str__(self):
        return "tc: " + str(self.tc) + " miktar: " + str(self.value) + " tarih : " + str(self.insert_date)


class Credit(models.Model):
    class Meta:
        verbose_name = 'Kredi verilen'
    record_id = models.AutoField(primary_key=True)
    tc = models.CharField(max_length=12,db_index=True)
    value = models.IntegerField(default=0)  # sandik aidat
    insert_date = models.DateTimeField()

    def __str__(self):
        return "tc: " + str(self.tc) + " miktar: " + str(self.value) + " tarih : " + str(self.insert_date)


class Outcome(models.Model):
    class Meta:
        verbose_name = 'Gider'
    record_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    value = models.IntegerField(default=0)  # sandik aidat
    insert_date = models.DateTimeField()


class Profit(models.Model):
    class Meta:
        verbose_name = 'Profit'
    record_id = models.AutoField(primary_key=True)
    tc = models.CharField(max_length=12, db_index=True)
    odenen_aidat = models.IntegerField(default=0)
    kar_payi =  models.IntegerField(default=0)