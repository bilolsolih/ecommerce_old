# Generated by Django 4.2 on 2023-04-20 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_discount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0002_shippingscope_deliveryservice_logo_and_more'),
        ('orders', '0004_alter_cart_options_alter_cartentry_cart_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=250, verbose_name='Address')),
                ('postal_code', models.CharField(max_length=20, verbose_name='Postal code')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('region', models.CharField(max_length=100, verbose_name='Region')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('street', models.CharField(max_length=100, verbose_name='Street')),
                ('paid', models.BooleanField(default=False, verbose_name='Paid')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='User who made this order')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.AlterModelOptions(
            name='cartentry',
            options={'verbose_name': 'Cart entry', 'verbose_name_plural': 'Cart entries'},
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('delivery_service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='services.deliveryservice', verbose_name='Delivery service')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='Parent order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='store.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Order item',
                'verbose_name_plural': 'Order items',
            },
        ),
    ]