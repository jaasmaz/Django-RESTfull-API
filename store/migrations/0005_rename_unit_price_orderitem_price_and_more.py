# Generated by Django 4.0.1 on 2022-01-18 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210610_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='unit_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='unit_price',
            new_name='price',
        ),
    ]
