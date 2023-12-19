from django.db import models

LOCATION_CHOICES = (
    ('LRBT', 'living room black table & around'),
    ('LRH', 'living room hanging'),
    ('LRWT', 'living room white tables'),
    ('BS', 'bookshelves'),
    ('OWS', 'outside window sill'),
    ('IWS', 'inside window sill - living room'),
    ('B1', 'bedroom 1'),
    ('B2', 'bedroom 2'),
    ('SC', 'special care')
)


class Plant(models.Model):
    name = models.CharField(max_length=200, default="", blank=True)
    location = models.CharField(choices=LOCATION_CHOICES, default='LRWT')
    frequency = models.IntegerField(default=1, blank=True, null=True)
    instructions = models.TextField(default="", blank=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
