from rest_framework.routers import DefaultRouter

from users.apps import UserConfig
from users.views import UserViewSet

app_name = UserConfig.name

router = DefaultRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [] + router.urls
