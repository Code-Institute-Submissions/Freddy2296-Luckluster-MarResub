# Generated by Django 3.1.2 on 2020-11-06 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_has_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock_level',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
