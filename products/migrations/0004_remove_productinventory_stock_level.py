# Generated by Django 3.2.9 on 2022-03-20 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_stock_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinventory',
            name='stock_level',
        ),
    ]
