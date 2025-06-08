from rest_framework.viewsets import ModelViewSet
from suppliers.models import Order, Product, Supplier
from suppliers.serializers import ProductSerializer, OrderSerializer, SupplierSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class SupplierViewSet(ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['country']
    ordering_fields = ['country']
