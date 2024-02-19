# Generated by Django 4.2.9 on 2024-01-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=20)),
                ('house_address', models.CharField(max_length=100)),
                ('house_type', models.CharField(max_length=100)),
                ('house_owner', models.CharField(max_length=100)),
                ('house_owner_phone', models.CharField(max_length=100)),
                ('house_owner_email', models.CharField(max_length=100)),
            ],
        ),
    ]
