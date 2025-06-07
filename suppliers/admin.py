from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

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
    @admin.action(description="Сlearing debt to suppliers at selected facilities")
    def clear_debt(self, request, queryset):
        updated = queryset.update(debt_to_supplier=0)
        self.message_user(
            request,
            ngettext(
                "%d debt was successfully cleared.",
                "%d debts was successfully cleared.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    list_display = (
        "id",
        "customer",
        "product",
        "supplier",
        "debt_to_supplier",
        "created_at",
        "level",
    )
    actions = [clear_debt]
