from rest_framework import serializers
from web.models import Plant
from django.contrib.auth.models import User

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'location', 'frequency', 'volume', 'instructions', 'photourl', 'status', 'start', 'end', 'added', 'changed']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
