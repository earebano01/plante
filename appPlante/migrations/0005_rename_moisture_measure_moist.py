# Generated by Django 4.2.7 on 2023-11-28 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appPlante', '0004_remove_measure_id_node_measure_num_node_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measure',
            old_name='moisture',
            new_name='moist',
        ),
    ]
