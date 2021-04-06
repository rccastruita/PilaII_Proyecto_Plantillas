# Generated by Django 3.1.7 on 2021-04-05 23:36

from django.db import migrations, models
import django.db.models.deletion
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Nombre_Producto', max_length=30)),
                ('description', models.TextField(default='')),
                ('image_1', models.ImageField(null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='products')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Category', max_length=30)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPresentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Regular', max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('inventory', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shopping.productcategory'),
        ),
    ]
