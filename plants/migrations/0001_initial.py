# Generated by Django 5.0.7 on 2024-07-21 14:05

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
                ("name", models.CharField(max_length=100)),
                ("about", models.TextField()),
                ("used_for", models.TextField()),
                ("image", models.ImageField(upload_to="plants/")),
                (
                    "category",
                    models.CharField(
                        choices=[("indoor", "Indoor"), ("outdoor", "Outdoor")],
                        max_length=100,
                    ),
                ),
                ("is_edible", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]