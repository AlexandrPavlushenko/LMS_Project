from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Имя пользователя"
    )
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Телефон"
    )
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Город")
    avatar = models.ImageField(
        upload_to="users/avatars/", null=True, blank=True, verbose_name="Аватар"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
