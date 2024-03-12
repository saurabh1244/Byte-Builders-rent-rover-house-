from django.db import models
from django.contrib.auth.models import User


class room_rent(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    room_prize = models.IntegerField()
    room_size = models.CharField(max_length=100)
    total_rooms = models.IntegerField()

    room_location = models.CharField(max_length=100)
    location_country = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    location_dist = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)



    line_bill_needed = models.BooleanField(default=False)
    room_allow = models.CharField(max_length=100)
    ROOM_CHOICES = [
        ('B', 'Boys'),
        ('G', 'Girls'),
    ]

    room_desc = models.TextField(max_length=200)
    room_for = models.CharField(max_length=1, choices=ROOM_CHOICES)
    smoking = models.BooleanField(default=False)
    drinking = models.BooleanField(default=False)

    room_images = models.ImageField(upload_to='images/')  # 'RoomImage' model defined below


class room_money(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE ,)
    amount = models.IntegerField()
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)



