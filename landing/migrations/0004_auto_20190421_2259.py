# Generated by Django 2.1.5 on 2019-04-21 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20190421_1914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'База Партнеров', 'verbose_name_plural': 'База Партнеров'},
        ),
        migrations.AlterModelTable(
            name='partners',
            table='Partners',
        ),
    ]
