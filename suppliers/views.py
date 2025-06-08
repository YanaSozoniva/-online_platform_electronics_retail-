from rest_framework.viewsets import ModelViewSet
from suppliers.models import Order, Product, Supplier
from suppliers.serializers import ProductSerializer, OrderSerializer, SupplierSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class SupplierViewSet(ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
