# Generated by Django 5.0.1 on 2024-01-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hospital", "0004_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("image", models.ImageField(upload_to="uploads/about")),
            ],
        ),
        migrations.DeleteModel(
            name="Contact",
        ),
    ]