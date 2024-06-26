# Generated by Django 5.0.4 on 2024-06-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0007_events_city"),
    ]

    operations = [
        migrations.CreateModel(
            name="InformationImage",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="information_images")),
            ],
        ),
    ]
