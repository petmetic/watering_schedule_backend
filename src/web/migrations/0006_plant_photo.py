# Generated by Django 5.0 on 2024-01-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0005_alter_plant_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="plant",
            name="photo",
            field=models.ImageField(default="", upload_to="uploads/"),
        ),
    ]