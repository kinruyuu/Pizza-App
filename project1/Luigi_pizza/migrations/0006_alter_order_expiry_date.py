# Generated by Django 5.0.1 on 2024-02-22 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Luigi_pizza', '0005_alter_order_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expiry_date',
            field=models.DateField(max_length=5, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
