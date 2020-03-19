from django.contrib import admin
import django.db.models

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
        "id",
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
        "zip_code",
        "transaction_type",
        "room_qty",
        "bedroom_qty",
    ]
    search_fields = ("city_label", "description")

    def get_queryset(self, request):
        qs = super(ListingAdmin, self).get_queryset(request)
        qs = qs.annotate(min_price=django.db.models.Min("pricings__price"))
        qs = qs.annotate(
            min_square_meter_price=django.db.models.Min("pricings__square_meter_price")
        )
        return qs

    def price(self, obj):
        return obj.min_price

    def square_meter_price(self, obj):
        return obj.min_square_meter_price

    price.admin_order_field = "min_price"
    square_meter_price.admin_order_field = "min_square_meter_price"
