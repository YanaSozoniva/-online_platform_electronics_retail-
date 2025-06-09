from rest_framework import serializers

from suppliers.models import Order, Product, Supplier


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    debt_to_supplier = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = Order
        fields = "__all__"
