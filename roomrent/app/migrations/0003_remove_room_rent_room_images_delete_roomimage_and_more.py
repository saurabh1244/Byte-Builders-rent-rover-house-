# Generated by Django 5.0 on 2024-03-11 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_room_rent_room_images_roomimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room_rent',
            name='room_images',
        ),
        migrations.DeleteModel(
            name='RoomImage',
        ),
        migrations.AddField(
            model_name='room_rent',
            name='room_images',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]