# Generated by Django 4.2.7 on 2024-01-24 13:37

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_remove_place_user_alter_place_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326),
        ),
    ]
