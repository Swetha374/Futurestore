# Generated by Django 4.0.6 on 2022-10-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_orders_delivery_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(null=True),
        ),
    ]
