# Generated by Django 4.0 on 2021-12-21 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_byword_student_constellation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='byword',
        ),
    ]