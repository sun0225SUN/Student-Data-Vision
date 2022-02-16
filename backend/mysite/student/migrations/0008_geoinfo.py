# Generated by Django 4.0 on 2021-12-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_sexinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('hometown', models.CharField(max_length=128, verbose_name='家乡')),
                ('value', models.CharField(default=0, max_length=128, verbose_name='家乡坐标')),
                ('coords', models.CharField(default=0, max_length=128, verbose_name='箭头坐标')),
            ],
            options={
                'verbose_name': '地图坐标',
                'verbose_name_plural': '地图坐标',
            },
        ),
    ]
