# Generated by Django 2.1 on 2018-08-15 14:27

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(choices=[(0, 'male'), (1, 'female'), (2, 'other')], default='male', max_length=100)),
                ('age', models.IntegerField(default=24)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Person')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='TimeFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sensor_data', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=8)),
                ('label', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Session')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
