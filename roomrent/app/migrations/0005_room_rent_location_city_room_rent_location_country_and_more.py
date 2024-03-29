# Generated by Django 5.0 on 2024-03-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_room_rent_room_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_rent',
            name='location_city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room_rent',
            name='location_country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room_rent',
            name='location_dist',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room_rent',
            name='location_state',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
