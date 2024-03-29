# Generated by Django 4.2.9 on 2024-01-23 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_alter_house_data_house_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_data',
            name='house_code',
            field=models.IntegerField(default=1, unique=True),
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('D_O_B', models.DateField()),
                ('Email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('Phone_No', models.CharField(max_length=10)),
                ('Room_No', models.IntegerField()),
                ('Tenant_image', models.ImageField(blank=True, upload_to='images/')),
                ('document', models.FileField(blank=True, upload_to='documents/')),
                ('Work_Place', models.CharField(blank=True, max_length=100, null=True)),
                ('Members', models.IntegerField(blank=True)),
                ('House', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.house_data')),
            ],
        ),
    ]
