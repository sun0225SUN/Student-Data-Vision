# Generated by Django 4.0 on 2021-12-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_anhuigeoinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvinceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='省份名称')),
                ('value', models.IntegerField(default=0, verbose_name='数值')),
            ],
            options={
                'verbose_name': '学生总数',
                'verbose_name_plural': '学生总数',
            },
        ),
        migrations.AlterModelOptions(
            name='anhuigeoinfo',
            options={'verbose_name': '省内学生', 'verbose_name_plural': '省内学生'},
        ),
        migrations.AlterModelOptions(
            name='geoinfo',
            options={'verbose_name': '省内学生', 'verbose_name_plural': '省内学生'},
        ),
    ]