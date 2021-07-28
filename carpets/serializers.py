from .models import *
from rest_framework import serializers

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = []

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        exclude = []

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        exclude = []

class CarpetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpet
        exclude = []

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        exclude = []

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        exclude = []

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


