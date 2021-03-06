# Generated by Django 3.2.2 on 2021-05-12 15:46

import App1.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeCompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequestForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_name', models.CharField(max_length=50)),
                ('bike_company', models.CharField(max_length=50)),
                ('bike_model', models.CharField(max_length=50)),
                ('bike_color', models.CharField(max_length=50)),
                ('pickup', models.CharField(max_length=50)),
                ('delivery', models.CharField(max_length=50)),
                ('kmcovered', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('problem', models.CharField(max_length=500)),
                ('completed', models.CharField(default='Not Completed', max_length=100)),
                ('serviceDate', models.DateField(validators=[App1.models.ServiceRequestForm.validate_date])),
                ('serviceTime', models.TimeField()),
                ('deliveryTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('bike_number', models.CharField(max_length=50)),
                ('bike_color', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.bikecompanymodel', to_field='companyName')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
