# Generated by Django 4.2.9 on 2024-02-15 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0042_old_payment_old_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='old_payment',
            name='Tenant_Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.old_record'),
        ),
    ]