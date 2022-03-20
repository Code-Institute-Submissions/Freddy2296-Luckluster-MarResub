# Generated by Django 3.2.9 on 2022-03-20 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productinventory_stock_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinventory',
            name='product',
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productinventory'),
        ),
    ]