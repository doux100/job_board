# Generated by Django 4.2.1 on 2023-05-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='jobrel',
            field=models.ManyToManyField(null=True, to='job.job'),
        ),
    ]
