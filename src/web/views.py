
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User


from web.models import Plant
from web.serializers import PlantSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows plant list to be viewed or edited.
    """

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticated]

