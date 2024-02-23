# Generated by Django 5.0.1 on 2024-01-12 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("dep_name", models.CharField(max_length=100)),
                ("dep_description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Slider",
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
                ("heading", models.CharField(max_length=250)),
                ("content", models.TextField(max_length=250)),
                ("image", models.ImageField(upload_to="slider")),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
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
                ("doc_name", models.CharField(max_length=255)),
                ("doc_spec", models.CharField(max_length=255)),
                ("doc_image", models.ImageField(upload_to="Doctors")),
                (
                    "dep_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
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
                ("p_name", models.CharField(max_length=255)),
                ("p_phone", models.CharField(max_length=255)),
                ("symptoms", models.CharField(max_length=300, null=True)),
                ("booking_date", models.DateField()),
                ("booked_on", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Pending", "Pending"),
                            ("Confirmed", "Confirmed"),
                            ("Canceled", "Canceled"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
                (
                    "doc_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.doctor",
                    ),
                ),
            ],
        ),
    ]