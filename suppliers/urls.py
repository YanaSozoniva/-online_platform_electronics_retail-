from rest_framework.routers import DefaultRouter

from suppliers.apps import SuppliersConfig
from suppliers.views import OrderViewSet, ProductViewSet, SupplierViewSet

app_name = SuppliersConfig.name

router = DefaultRouter()
router.register("order", OrderViewSet, basename="order")
router.register("product", ProductViewSet, basename="product")
router.register("supplier", SupplierViewSet, basename="supplier")

urlpatterns = [] + router.urls
