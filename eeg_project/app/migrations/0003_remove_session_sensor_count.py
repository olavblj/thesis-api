# Generated by Django 2.1 on 2018-09-12 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_session_real_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='sensor_count',
        ),
    ]
