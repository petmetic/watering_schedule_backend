# Generated by Django 5.0 on 2024-01-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Plant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=200)),
                (
                    "location",
                    models.CharField(
                        choices=[
                            ("living_room_black", "living room black table & around"),
                            ("living_room_hanging", "living room hanging"),
                            ("living_room_white", "living room white tables"),
                            ("bookshelves", "bookshelves"),
                            ("window_outside", "outside window sill"),
                            ("window_inside", "inside window sill - living room"),
                            ("bedroom1", "bedroom 1"),
                            ("bedroom2", "bedroom 2"),
                            ("special_care", "special care"),
                        ],
                        default="living_room_white",
                        max_length=100,
                    ),
                ),
                ("frequency", models.IntegerField(blank=True, default=1, null=True)),
                (
                    "volume",
                    models.CharField(
                        choices=[
                            ("100_ml", "100 ml"),
                            ("200_ml", "200 ml"),
                            ("300_ml", "300 ml"),
                            ("400_ml", "400 ml"),
                            ("500_ml", "500 ml"),
                        ],
                        default="100_ml",
                        max_length=100,
                    ),
                ),
                ("instructions", models.TextField(blank=True, default="")),
                ("start", models.DateTimeField(blank=True, null=True)),
                ("end", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("watered", "watered"),
                            ("needs_watering", "needs watering"),
                        ],
                        default="needs_watering",
                        max_length=100,
                    ),
                ),
                ("added", models.DateTimeField(auto_now_add=True)),
                ("changed", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]
