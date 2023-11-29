# Generated by Django 4.2.7 on 2023-11-22 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPlante', '0002_rename_height_measure_light_remove_measure_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='measure',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='measure',
            name='moisture',
            field=models.IntegerField(null=True),
        ),
    ]
