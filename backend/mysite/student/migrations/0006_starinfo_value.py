# Generated by Django 4.0 on 2021-12-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_starinfo_alter_student_constellation'),
    ]

    operations = [
        migrations.AddField(
            model_name='starinfo',
            name='value',
            field=models.IntegerField(default=0, verbose_name='数值'),
        ),
    ]
