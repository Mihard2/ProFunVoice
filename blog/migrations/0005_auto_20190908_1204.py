# Generated by Django 2.1.1 on 2019-09-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190908_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='longgrid',
            name='date_pub',
            field=models.DateTimeField(blank=True, verbose_name='Создан'),
        ),
    ]
