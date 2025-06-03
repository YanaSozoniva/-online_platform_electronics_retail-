from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = models.CharField(unique=True, verbose_name="Ник")
    email = models.EmailField(
        verbose_name="Email",
        null=True,
        blank=True,
    )
    phone = PhoneNumberField(verbose_name="Телефон", null=True, blank=True, help_text="Введите номер телефона")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
