# Generated by Django 3.1.7 on 2021-06-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_payments', '0002_payment_purchase_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]