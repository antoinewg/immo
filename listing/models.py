from django.db import models

import listing.enums


class Contact(models.Model):
    agency_id = models.IntegerField(primary_key=True)
    agency_page = models.URLField()
    contact_name = models.CharField(max_length=256)
    img_url = models.URLField()
    phone_number = models.CharField(max_length=10)
    email = models.BooleanField()
    agency_link = models.URLField()


class Listing(models.Model):
    id = models.IntegerField(primary_key=True)
    first_saved_at = models.DateTimeField(auto_now_add=True)
    publication_id = models.IntegerField()
    highlighting_level = models.IntegerField()
    business_unit = models.IntegerField()
    estate_type = models.CharField(
        choices=listing.enums.choices(listing.enums.ESTATE_TYPE), max_length=48
    )
    room_qty = models.IntegerField()
    bedroom_qty = models.IntegerField()
    square_meter = models.IntegerField()
    transaction_type = models.IntegerField()
    nature = models.IntegerField()
    contact = models.ForeignKey(
        Contact, on_delete=models.PROTECT, related_name="listing"
    )
    service_url = models.URLField()
    is_exlusive = models.BooleanField()
    city_label = models.CharField(max_length=48)
    zip_code = models.IntegerField(db_index=True)
    description = models.TextField()
    video_url = models.URLField()
    virtual_visit_url = models.URLField()
    classified_url = models.URLField()


class Pricing(models.Model):
    uid = models.UUIDField(primary_key=True)
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
    uid = models.UUIDField(primary_key=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.PROTECT, related_name="photos"
    )
    photo_url = models.URLField()
