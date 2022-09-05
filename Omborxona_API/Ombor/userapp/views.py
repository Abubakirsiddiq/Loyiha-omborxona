from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from Ombor.userapp.models import Ombor
from Ombor.userapp.serializers import OmborSer


class OmborAPIView(APIView):
    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        ser = OmborSer(ombor)
        return Response(ser.data)

