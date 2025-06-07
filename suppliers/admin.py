from django.contrib import admin

from suppliers.models import Supplier, Order, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели поставщик"""

    list_display = (
        "id",
        "name",
        "email",
        "country",
        "address",
        "city",
        "type",
    )
    list_filter = ("city", "name")
    search_fields = (
        "city", "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели продукт"""

    list_display = (
        "id",
        "name",
        "model_product",
        "release_date",
    )
    list_filter = ("name", )
    search_fields = (
        "name", "model_product",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели заказ"""

    list_display = (
        "id",
        "customer",
        "product",
        "supplier",
        "debt_to_supplier",
        "created_at",
        "level",
    )
