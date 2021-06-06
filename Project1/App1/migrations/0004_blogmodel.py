# Generated by Django 3.2.2 on 2021-05-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_ourservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=500)),
                ('blogImage', models.ImageField(upload_to='')),
                ('blogContent', models.TextField()),
                ('blogLink', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]