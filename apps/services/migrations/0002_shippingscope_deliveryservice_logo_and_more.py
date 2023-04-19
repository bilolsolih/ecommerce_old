# Generated by Django 4.2 on 2023-04-19 12:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingScope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=255, verbose_name='Shipping scope type')),
            ],
            options={
                'verbose_name': 'Shipping scope type',
                'verbose_name_plural': 'Shipping scope types',
            },
        ),
        migrations.AddField(
            model_name='deliveryservice',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/services/logos/', verbose_name='Delivery service logo'),
        ),
        migrations.AlterField(
            model_name='deliveryservice',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Delivery service name'),
        ),
        migrations.CreateModel(
            name='PriceRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('quantity_from', models.DecimalField(decimal_places=2, default=0, max_digits=24, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Beginning from')),
                ('quantity_to', models.DecimalField(decimal_places=2, default=0, max_digits=24, validators=[django.core.validators.MinValueValidator(0)], verbose_name='To and including')),
                ('price_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=24, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price per kilometer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_ranges', to='services.deliveryservice', verbose_name='Related parent service')),
            ],
            options={
                'verbose_name': 'Price range',
                'verbose_name_plural': 'Price ranges',
                'ordering': ['quantity_from'],
            },
        ),
        migrations.AlterField(
            model_name='supplier',
            name='shipping_scope',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='suppliers', to='services.shippingscope', verbose_name='Shipping scope'),
        ),
    ]