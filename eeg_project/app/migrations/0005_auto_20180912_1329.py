# Generated by Django 2.1 on 2018-09-12 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180912_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='real_data',
            new_name='is_real_data',
        ),
    ]
