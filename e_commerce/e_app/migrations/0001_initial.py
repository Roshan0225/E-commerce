# Generated by Django 5.0.6 on 2024-08-22 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='consumer',
            fields=[
                ('S_No', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.TextField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('Phone', models.BigIntegerField(null=True)),
                ('Gender', models.TextField(max_length=10, null=True)),
                ('Address', models.TextField(max_length=1000, null=True)),
                ('Password', models.TextField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller_reg',
            fields=[
                ('S_No', models.AutoField(primary_key=True, serialize=False)),
                ('Seller_name', models.TextField(max_length=100, null=True)),
                ('Photo', models.ImageField(upload_to='seller_photo/')),
                ('Seller_email', models.EmailField(max_length=100, null=True)),
                ('Phone', models.BigIntegerField(null=True)),
                ('Gender', models.TextField(max_length=10, null=True)),
                ('Address', models.TextField(max_length=1000, null=True)),
                ('Password', models.TextField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('No', models.AutoField(primary_key=True, serialize=False)),
                ('sellerid', models.IntegerField()),
                ('Seller_name', models.TextField(max_length=100, null=True)),
                ('Seller_address', models.TextField(max_length=1000, null=True)),
                ('product_name', models.TextField(max_length=100)),
                ('product_image', models.ImageField(upload_to='buyer/')),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('buyeddate', models.DateTimeField(auto_now_add=True)),
                ('seller_contact_number', models.BigIntegerField()),
                ('seller_email_id', models.EmailField(max_length=100)),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_app.consumer')),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('No', models.AutoField(primary_key=True, serialize=False)),
                ('Seller_email', models.EmailField(max_length=100)),
                ('Product', models.TextField(max_length=100, null=True)),
                ('product_Photo', models.ImageField(upload_to='product_img/')),
                ('Specification', models.TextField(max_length=300, null=True)),
                ('Quantity', models.IntegerField(null=True)),
                ('Price', models.IntegerField(null=True)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_app.seller_reg')),
            ],
        ),
    ]
