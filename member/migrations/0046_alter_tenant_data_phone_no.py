# Generated by Django 4.2.9 on 2024-02-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0045_payments_data_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant_data',
            name='Phone_No',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
