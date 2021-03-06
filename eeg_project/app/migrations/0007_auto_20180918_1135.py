# Generated by Django 2.1 on 2018-09-18 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180918_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timeframe',
            name='label',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='timeframes', to='app.Label'),
            preserve_default=False,
        ),
    ]
