# Generated by Django 4.2.9 on 2024-01-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0018_alter_tenant_data_work_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant_data',
            name='Members_Name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]