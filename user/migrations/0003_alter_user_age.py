# Generated by Django 4.1.3 on 2022-12-04 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
    ]