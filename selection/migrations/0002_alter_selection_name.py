# Generated by Django 4.1.3 on 2022-12-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Наименование'),
        ),
    ]
