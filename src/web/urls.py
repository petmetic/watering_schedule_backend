from rest_framework import routers
from django.urls import include, path

from web import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"plants", views.PlantViewSet)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]

urlpatterns += router.urls
