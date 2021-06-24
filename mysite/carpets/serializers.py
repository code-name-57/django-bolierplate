from .models import *
from rest_framework import serializers

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = []

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        exclude = []

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        exclude = []

class CarpetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpet
        exclude = []


