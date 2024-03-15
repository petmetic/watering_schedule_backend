from django.db import models


class Plant(models.Model):
    LOCATION_CHOICES = (
        ("living_room_black", "living room black table & around"),
        ("living_room_hanging", "living room hanging"),
        ("living_room_white", "living room white tables"),
        ("bookshelves", "bookshelves"),
        ("window_outside", "outside window sill"),
        ("window_inside", "inside window sill - living room"),
        ("bedroom1", "bedroom 1"),
        ("bedroom2", "bedroom 2"),
        ("special_care", "special care"),
    )

    WATER_VOLUME = (
        ("100_ml", "100 ml"),
        ("200_ml", "200 ml"),
        ("300_ml", "300 ml"),
        ("400_ml", "400 ml"),
        ("500_ml", "500 ml"),
    )
    STATUS = (("watered", "watered"), ("needs_watering", "needs watering"))

    name = models.CharField(max_length=200, default="")
    location = models.CharField(
        max_length=100, choices=LOCATION_CHOICES, default="living room white tables"
    )
    frequency = models.IntegerField(default=1, blank=True, null=True)
    volume = models.CharField(max_length=100, choices=WATER_VOLUME, default="100 ml")
    instructions = models.TextField(default="", blank=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS, default="needs watering")
    photo = models.ImageField(max_length=None, default="")
    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
