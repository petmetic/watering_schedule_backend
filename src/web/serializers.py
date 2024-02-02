from django.contrib.auth.models import User
from rest_framework import serializers

from web.models import Plant


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = [
            "id",
            "name",
            "location",
            "frequency",
            "volume",
            "instructions",
            "photo",
            "status",
            "start",
            "end",
            "added",
            "changed",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]
