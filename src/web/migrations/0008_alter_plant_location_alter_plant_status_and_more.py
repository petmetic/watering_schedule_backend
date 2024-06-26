# Generated by Django 5.0 on 2024-02-20 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0007_alter_plant_location_alter_plant_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plant",
            name="location",
            field=models.CharField(
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
                default="living room white tables",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="plant",
            name="status",
            field=models.CharField(
                choices=[("watered", "watered"), ("needs_watering", "needs watering")],
                default="needs watering",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="plant",
            name="volume",
            field=models.CharField(
                choices=[
                    ("100_ml", "100 ml"),
                    ("200_ml", "200 ml"),
                    ("300_ml", "300 ml"),
                    ("400_ml", "400 ml"),
                    ("500_ml", "500 ml"),
                ],
                default="100 ml",
                max_length=100,
            ),
        ),
    ]
