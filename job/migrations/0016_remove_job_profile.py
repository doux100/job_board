# Generated by Django 4.2.1 on 2023-05-15 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_alter_job_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='profile',
        ),
    ]