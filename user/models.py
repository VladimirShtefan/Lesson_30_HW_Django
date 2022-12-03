from django.db import models
from django.contrib.auth.models import AbstractUser

from location.models import Location


class User(AbstractUser):
    ROLES = [
        ('member', 'Пользователь'),
        ('admin', 'Администратор'),
        ('moderator', 'Модератор'),
    ]

    role = models.CharField(max_length=9, choices=ROLES, default="member", verbose_name='Роль')
    age = models.SmallIntegerField(verbose_name='Возраст')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Местоположение')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username
