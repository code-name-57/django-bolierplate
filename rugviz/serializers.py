from .models import *
from rest_framework import serializers

class EnvColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvColor
        exclude = []

class FloorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorType
        exclude = []

class FloorTextureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorTexture
        exclude = []


