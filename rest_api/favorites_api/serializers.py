from accounts.models import *
from rest_framework import serializers


class SceneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SceneImage
        exclude = []

class FavoriteItemSerializer(serializers.ModelSerializer):
    sceneimage_set = SceneImageSerializer(many=True)
    class Meta:
        model = FavoriteItem
        exclude = []

class FavoriteListSerializer(serializers.ModelSerializer):
    favoriteitem_set = FavoriteItemSerializer(many=True)
    class Meta:
        model = FavoriteList
        exclude = []
