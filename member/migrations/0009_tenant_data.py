# Generated by Django 4.2.9 on 2024-01-23 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_delete_tenant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, unique=True)),
                ('D_O_B', models.DateField()),
                ('Email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('Phone_No', models.CharField(max_length=10, unique=True)),
                ('Room_No', models.IntegerField()),
                ('Tenant_image', models.ImageField(upload_to='images/')),
                ('document', models.FileField(upload_to='documents/')),
                ('Work_Place', models.CharField(blank=True, max_length=100, null=True)),
                ('Members', models.IntegerField(blank=True)),
                ('Rent', models.CharField(max_length=5)),
                ('Advance', models.CharField(max_length=5)),
                ('Arrived_Month', models.DateField()),
                ('House', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.house_data')),
            ],
        ),
    ]
