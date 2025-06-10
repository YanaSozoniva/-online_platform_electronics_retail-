from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ngettext

from suppliers.models import Order, Product, Supplier


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
        "city",
        "name",
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
    list_filter = ("name",)
    search_fields = (
        "name",
        "model_product",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели заказ"""

    @admin.action(description="Очистить задолжность перед поставщиком у выбранных объектов")
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
        "get_supplier_link",
        "debt_to_supplier",
        "created_at",
        "level",
    )
    actions = [clear_debt]
    list_filter = ("supplier__city",)

    def get_supplier_link(self, obj):
        url = reverse("admin:suppliers_supplier_change", args=[obj.supplier.id])
        return format_html('<a href="{}">{}</a>', url, obj.supplier.name)

    get_supplier_link.short_description = "Поставщик"
