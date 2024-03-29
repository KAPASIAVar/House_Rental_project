# Generated by Django 4.2.9 on 2024-02-15 08:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0041_delete_old_payment_delete_old_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Old_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tenant_Name', models.CharField(max_length=50, null=True)),
                ('House_Name', models.CharField(max_length=50, null=True)),
                ('Rent_Amount', models.IntegerField()),
                ('Date', models.DateField()),
                ('Mode', models.CharField(max_length=20)),
                ('Payment_Screenshot', models.ImageField(blank=True, upload_to='payments/')),
                ('Previous_Electricity_Unit', models.IntegerField()),
                ('Current_Electricity_Unit', models.IntegerField()),
                ('Total_Bill', models.IntegerField()),
                ('Unit_Price', models.IntegerField()),
                ('Water_Bill', models.IntegerField()),
                ('Total_Amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Old_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_No', models.IntegerField(null=True)),
                ('Tenant_Name', models.CharField(max_length=50)),
                ('House_Name', models.CharField(max_length=50)),
                ('D_O_B', models.DateField()),
                ('Address', models.CharField(blank=True, max_length=200)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Date', models.DateField()),
                ('Checkin_Date', models.DateField()),
                ('Phone_No', models.CharField(max_length=10)),
                ('Tenant_image', models.ImageField(blank=True, upload_to='old_photo/')),
                ('Rent', models.CharField(max_length=10)),
                ('Documents_Upload', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
            ],
        ),
    ]
