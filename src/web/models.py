from django.db import models

LOCATION_CHOICES = (
    ('living_room_black', 'living room black table & around'),
    ('living_room_hanging', 'living room hanging'),
    ('living_room_white', 'living room white tables'),
    ('bookshelves', 'bookshelves'),
    ('window_outside', 'outside window sill'),
    ('window_inside', 'inside window sill - living room'),
    ('bedroom1', 'bedroom 1'),
    ('bedroom2', 'bedroom 2'),
    ('special_care', 'special care')
)


class Plant(models.Model):
    name = models.CharField(max_length=200, default="")
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='living_room_white')
    frequency = models.IntegerField(default=1, blank=True, null=True)
    instructions = models.TextField(default="", blank=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']