from django.db import models


class Plant(models.Model):
    LOCATION_CHOICES = (
        ("living room black table & around", "living_room_black"),
        (
            "living room hanging",
            "living_room_hanging",
        ),
        ("living room white tables", "living_room_white"),
        ("bookshelves", "bookshelves"),
        ("outside window sill", "window_outside"),
        ("inside window sill - living room", "window_inside"),
        ("bedroom 1", "bedroom1"),
        ("bedroom 2", "bedroom2"),
        ("special care", "special_care"),
    )

    WATER_VOLUME = (
        ("100 ml", "100 ml"),
        ("200 ml", "200 ml"),
        ("300 ml", "300 ml"),
        ("400 ml", "400 ml"),
        ("500 ml", "500 ml"),
    )
    STATUS = (("watered", "watered"), ("needs watering", "needs watering"))

    name = models.CharField(max_length=200, default="")
    location = models.CharField(
        max_length=100, choices=LOCATION_CHOICES, default="living_room_white"
    )
    frequency = models.IntegerField(default=1, blank=True, null=True)
    volume = models.CharField(max_length=100, choices=WATER_VOLUME, default="100_ml")
    instructions = models.TextField(default="", blank=True)
    start = models.DateTimeField(blank=True, null=True)
    photourl = models.CharField(max_length=200, default="")
    end = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS, default="needs_watering")

    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
