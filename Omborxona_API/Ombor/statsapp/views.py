from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Stats
from .serializers import StatsSer


class StatslarAPIView(APIView):
    def get(self, request):
        mahsulotlar = Stats.objects.filter(user=request.user)
        ser = StatsSer(mahsulotlar)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = StatsSer(data=malumot)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class StatsAPIView(APIView):
    def put(self, request, pk):
        client = Stats.objects.get(id=pk)
        ser = StatsSer(client)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)

