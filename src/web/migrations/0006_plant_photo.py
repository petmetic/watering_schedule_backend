# Generated by Django 5.0 on 2024-02-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0005_remove_plant_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="plant",
            name="photo",
            field=models.ImageField(default="", upload_to=""),
        ),
    ]