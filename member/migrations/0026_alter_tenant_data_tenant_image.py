# Generated by Django 4.2.9 on 2024-02-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0025_payments_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant_data',
            name='Tenant_image',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
