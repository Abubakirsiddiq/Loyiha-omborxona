from django.db import models
from userapp.models import *
from Ombor.asosiy.models import Mahsulot, Client
from Ombor.userapp.models import Ombor


class Stats(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, models.SET_NULL, null=True)
    client = models.ForeignKey(Client, models.SET_NULL, null=True)
    sana = models.DateTimeField(auto_now_add=True)
    miqdor = models.IntegerField(default=0)
    umumiy = models.PositiveBigIntegerField()
    talandi = models.PositiveBigIntegerField()
    nasiya = models.PositiveBigIntegerField(default=0)
    ombor = models.ForeignKey(Ombor, models.SET_NULL, null=True)

