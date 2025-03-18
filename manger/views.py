from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.response import Response
# Create your views here.
class MangerView(APIView):

    def get(self,request):
        manger = Manger.objects.all()
        serializer = MangerSerializer(instance=manger,many=True)
        return Response(serializer.data)

