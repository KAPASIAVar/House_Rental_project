# Generated by Django 4.2.9 on 2024-02-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0026_alter_tenant_data_tenant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments_data',
            name='Payment_Screenshot',
            field=models.ImageField(blank=True, upload_to='payments/'),
        ),
    ]