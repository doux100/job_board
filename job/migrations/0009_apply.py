# Generated by Django 4.2.1 on 2023-05-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_slug_alter_job_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('cover', models.TextField(max_length=500)),
            ],
        ),
    ]
