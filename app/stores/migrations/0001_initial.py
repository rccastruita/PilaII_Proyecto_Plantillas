# Generated by Django 3.1.7 on 2021-04-05 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Torreón', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Store', max_length=40)),
                ('direccion', models.CharField(default='Calle 12 #123', max_length=60)),
                ('zip_code', models.CharField(default='27123', max_length=10)),
                ('phone_number', models.CharField(default='8711234567', max_length=15)),
                ('email', models.EmailField(default='mymail@bakery.com', max_length=254)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.city')),
            ],
        ),
    ]