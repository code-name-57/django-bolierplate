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

class CarpetPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarpetPicture
        fields = ('id', 'carpet', 'image')