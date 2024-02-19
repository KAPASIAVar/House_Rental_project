# Generated by Django 4.2.9 on 2024-02-06 12:26

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0032_delete_old_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Old_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tenant_Name', models.CharField(max_length=50)),
                ('House_Name', models.CharField(max_length=50)),
                ('D_O_B', models.DateField()),
                ('Address', models.CharField(blank=True, max_length=200)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('Date', models.DateField()),
                ('Phone_No', models.IntegerField()),
                ('Tenant_image', models.ImageField(blank=True, upload_to='old_photo/')),
                ('Rent', models.CharField(max_length=10)),
                ('Documents_Upload', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
            ],
        ),
    ]
