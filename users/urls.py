from django.urls import path
from rest_framework.routers import DefaultRouter

from suppliers.views import UserViewSet
from users.apps import UserConfig

app_name = UserConfig.name

router = DefaultRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [

] + router.urls
