# Generated by Django 3.0.4 on 2020-03-18 22:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("agency_id", models.IntegerField(primary_key=True, serialize=False)),
                ("agency_page", models.URLField()),
                ("contact_name", models.CharField(max_length=256)),
                ("img_url", models.URLField()),
                ("phone_number", models.CharField(max_length=32)),
                ("email", models.BooleanField()),
                ("agency_link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Listing",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("first_saved_at", models.DateTimeField(auto_now_add=True)),
                ("last_saved_at", models.DateTimeField(auto_now=True)),
                ("publication_id", models.IntegerField()),
                ("highlighting_level", models.IntegerField()),
                ("business_unit", models.IntegerField()),
                ("photos_qty", models.IntegerField(default=-1)),
                ("elevator_qty", models.IntegerField(default=0)),
                ("floor", models.IntegerField(default=-1)),
                (
                    "estate_type",
                    models.CharField(
                        choices=[("appartment", "Appartement")], max_length=48
                    ),
                ),
                ("room_qty", models.IntegerField(default=-1)),
                ("bedroom_qty", models.IntegerField(default=-1)),
                ("square_meter", models.IntegerField()),
                ("transaction_type", models.IntegerField()),
                ("nature", models.IntegerField()),
                ("service_url", models.URLField()),
                ("is_exlusive", models.BooleanField(blank=True, null=True)),
                ("city_label", models.CharField(max_length=48)),
                ("district_label", models.CharField(max_length=100)),
                ("zip_code", models.IntegerField(db_index=True)),
                ("description", models.TextField()),
                ("video_url", models.URLField(blank=True, null=True)),
                ("virtual_visit_url", models.URLField(blank=True, null=True)),
                ("classified_url", models.URLField(blank=True, null=True)),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="listing",
                        to="listing.Contact",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pricing",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("price", models.IntegerField(db_index=True)),
                ("square_meter_price", models.IntegerField()),
                ("monthly_price", models.IntegerField()),
                ("lifetime", models.BooleanField()),
                ("loan_service_url", models.URLField()),
                ("first_saved_at", models.DateTimeField(auto_now_add=True)),
                (
                    "listing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pricings",
                        to="listing.Listing",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("photo_url", models.URLField()),
                (
                    "listing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="photos",
                        to="listing.Listing",
                    ),
                ),
            ],
        ),
    ]
