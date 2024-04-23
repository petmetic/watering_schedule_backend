from rest_framework.routers import DefaultRouter

from web import views


router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"plants", views.PlantViewSet)
