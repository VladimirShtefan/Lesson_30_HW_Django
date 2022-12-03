from django.db import models
from rest_framework import serializers


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
