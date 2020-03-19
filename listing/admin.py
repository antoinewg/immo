from django.contrib import admin
from django.utils.text import Truncator

from . import models


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["uid", "listing"]
    fields = ("uid", "listing", "photo_url")


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["agency_id", "contact_name"]
    list_filter = ["agency_id", "contact_name"]


@admin.register(models.Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ["uid", "price", "square_meter_price"]
    date_hierarchy = "first_saved_at"


@admin.register(models.Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = [
        "classified_url",
        "square_meter",
        "price",
        "square_meter_price",
        "room_qty",
        "bedroom_qty",
        "transaction_type",
        "zip_code",
    ]
    date_hierarchy = "first_saved_at"
    list_filter = [
        "estate_type",
        "room_qty",
        "bedroom_qty",
        "transaction_type",
        "zip_code",
    ]
    search_fields = ("city_label", "description")
