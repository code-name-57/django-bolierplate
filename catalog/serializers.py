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