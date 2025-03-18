from rest_framework import serializers
from .models import *
class MangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manger
        fields = '__all__'
