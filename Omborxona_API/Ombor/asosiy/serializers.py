from rest_framework import serializers
from .models import *


class ClientSer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "all"


class MahsulotSer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = "__all__"

