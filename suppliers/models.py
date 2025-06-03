import datetime

from django.db import models
from users.models import User


class Product(models.Model):
    """Класс для создания модели(таблицы) Продукты"""

    name = models.CharField(max_length=50, verbose_name="Название", help_text="Введите название товара")
    model_product = models.CharField(
        max_length=200, verbose_name="Модель", help_text="Введите модель ", blank=True, null=True
    )
    release_date = models.DateField(
        verbose_name="Дата выхода",
        help_text="Введите дату выхода продукта на рынок",
        default=datetime.datetime.today(),
    )

    def __str__(self):
        """Метод для строкового отображения информации о категории"""
        return self.name

    class Meta:
        """Данный класс используется для добавления метаданных к модели:
        наименование модели в единственном и множественном числе"""

        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"