# Generated by Django 4.2.9 on 2024-02-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0035_old_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='old_record',
            name='Room_No',
            field=models.IntegerField(null=True),
        ),
    ]
