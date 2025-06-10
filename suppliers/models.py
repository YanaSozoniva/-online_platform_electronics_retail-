from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Product(models.Model):
    """Класс для создания модели(таблицы) Продукты"""

    name = models.CharField(max_length=50, verbose_name="Название", help_text="Введите название товара")
    model_product = models.CharField(
        max_length=200, verbose_name="Модель", help_text="Введите модель ", blank=True, null=True
    )
    release_date = models.DateField(
        verbose_name="Дата выхода",
        help_text="Введите дату выхода продукта на рынок",
        default=timezone.now,
    )

    def __str__(self):
        """Метод для строкового отображения информации о продукте"""
        return self.name

    class Meta:
        """Данный класс используется для добавления метаданных к модели:
        наименование модели в единственном и множественном числе"""

        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Supplier(models.Model):
    """Класс для создания модели(таблицы) Поставщик"""

    name = models.CharField(
        max_length=100, verbose_name="Название фирмы", help_text="Введите название фирмы-постащика"
    )
    email = models.EmailField(
        verbose_name="Email",
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=100, verbose_name="Страна", help_text="Введите страну", blank=True, null=True
    )
    city = models.CharField(
        max_length=100, verbose_name="Город", help_text="Введите название фирмы-поставщика", blank=True, null=True
    )
    address = models.TextField(
        verbose_name="Адрес поставщика",
        help_text="Введите адрес фирмы-поставщика (улица, № дома)",
        blank=True,
        null=True,
    )
    FACTORY = "factory"
    RETAIL = "retail"
    ENTREPRENEUR = "entrepreneur"

    TYPE_CHOICES = [
        (FACTORY, "завод"),
        (RETAIL, "розничная сеть"),
        (ENTREPRENEUR, "индивидуальный предприниматель"),
    ]

    type = models.CharField(max_length=35, choices=TYPE_CHOICES, default=FACTORY, verbose_name="тип юридического лица")

    def __str__(self):
        """Метод для строкового отображения информации о поставщиках"""
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class Order(models.Model):
    """Класс для создания модели(таблицы) Заказ"""

    customer = models.ForeignKey(
        to=Supplier,
        on_delete=models.CASCADE,
        verbose_name="Заказчик",
        help_text="Введите заказчика",
        related_name="order_customer",
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name="Товара",
        help_text="Введите товар",
        related_name="orders",
    )

    supplier = models.ForeignKey(
        to=Supplier,
        on_delete=models.CASCADE,
        verbose_name="Поставщик",
        help_text="Введите поставщика",
        related_name="orders",
    )

    debt_to_supplier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Задолжность",
        help_text="Укажите задолжность перед поставщиком",
        default=0,
    )
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    level = models.PositiveIntegerField(
        verbose_name="Уровень в иерархии", validators=[MinValueValidator(0), MaxValueValidator(2)]
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
