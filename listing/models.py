import uuid

from django.db import models

import listing.enums


class Contact(models.Model):
    agency_id = models.IntegerField(primary_key=True)
    agency_page = models.URLField()
    contact_name = models.CharField(max_length=256)
    img_url = models.URLField()
    phone_number = models.CharField(max_length=32)
    email = models.BooleanField()
    agency_link = models.URLField()


class Listing(models.Model):
    id = models.IntegerField(primary_key=True)
    first_saved_at = models.DateTimeField(auto_now_add=True)
    last_saved_at = models.DateTimeField(auto_now=True)
    publication_id = models.IntegerField()
    highlighting_level = models.IntegerField()
    business_unit = models.IntegerField()
    photos_qty = models.IntegerField(default=-1)
    elevator_qty = models.IntegerField(default=0)
    floor = models.IntegerField(default=-1)
    estate_type = models.CharField(
        choices=listing.enums.choices(listing.enums.ESTATE_TYPE), max_length=48
    )
    room_qty = models.IntegerField(default=-1)
    bedroom_qty = models.IntegerField(default=-1)
    square_meter = models.IntegerField()
    transaction_type = models.IntegerField()
    nature = models.IntegerField()
    contact = models.ForeignKey(
        Contact, on_delete=models.PROTECT, related_name="listing"
    )
    service_url = models.URLField()
    is_exlusive = models.BooleanField(blank=True, null=True)
    city_label = models.CharField(max_length=48)
    district_label = models.CharField(max_length=100)
    zip_code = models.IntegerField(db_index=True)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    virtual_visit_url = models.URLField(blank=True, null=True)
    classified_url = models.URLField(blank=True, null=True)


class Pricing(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    price = models.IntegerField(db_index=True)
    square_meter_price = models.IntegerField()
    monthly_price = models.IntegerField()
    lifetime = models.BooleanField()
    loan_service_url = models.URLField()
    first_saved_at = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.PROTECT, related_name="pricings"
    )


class Photo(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    listing = models.ForeignKey(
        Listing, on_delete=models.PROTECT, related_name="photos"
    )
    photo_url = models.URLField()
