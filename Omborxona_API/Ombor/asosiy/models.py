from django.db import models
from django.db import models
from userapp.models import Ombor


class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    kelgan_narx = models.IntegerField()
    sotuv_narx = models.IntegerField()
    miqdor = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)


class Client(models.Model):
    dokon = models.CharField(max_length=50)
    ism = models.CharField(max_length=50)
    telefon = models.CharField(max_length=15)
    manzil = models.CharField(max_length=100)
    qarz = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)

