from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Oznaka(models.Model):
    naziv = models.CharField(max_length=200)

    def __str__(self):
        return self.naziv

class Plan(models.Model):
    naziv=models.CharField(max_length=150)
    cijena=models.IntegerField()
    oznake=models.ManyToManyField(Oznaka, default=None, blank=True, related_name='oznake')

    def __str__(self):
        return '%s' % self.naziv


class Trener(models.Model):
    ime=models.CharField(max_length=150)
    image=models.ImageField(upload_to='team/', default=None)

    def __str__(self):
        return self.ime
    

class Pretplatnik(models.Model):
    korisnik=models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    trener=models.ForeignKey(Trener, on_delete=models.CASCADE, null=True)
    plan=models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    datum_r=models.DateField(blank=True,null=True)
    spol=models.CharField(max_length=25, default=None)
    adresa=models.CharField(max_length=150, null=True)

    def __str__(self):
        return str(self.korisnik)

class Pretplata(models.Model):
    pretplatnik=models.ForeignKey(Pretplatnik, on_delete=models.CASCADE, null=True)
    plan=models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)




