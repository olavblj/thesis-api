# Generated by Django 2.1 on 2018-09-12 12:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_session_sensor_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='sensor_names',
        ),
        migrations.AddField(
            model_name='session',
            name='ch_names',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), default=['C3', 'C4', 'P3', 'P4'], size=8),
            preserve_default=False,
        ),
    ]
