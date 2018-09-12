# Generated by Django 2.1 on 2018-09-12 11:35

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=100)),
                ('age', models.IntegerField()),
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
                ('sensor_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), default=list, size=8)),
                ('sensor_count', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='app.Person')),
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
                ('timestamp', models.FloatField()),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeframes', to='app.Label')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeframes', to='app.Session')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
