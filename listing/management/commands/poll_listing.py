import parser.utils as utils
import time

from django.core.management.base import BaseCommand

from listing.enums import ESTATE_TYPE
import listing.models as models


SIZE = 25


class Command(BaseCommand):
    help = "Recursively poll listings."

    def handle(self, *args, **options):
        total = 0
        cont = True
        utils.log(f"Started polling of listings...")
        while cont:
            listings = utils.fetch_batch_listing(start=total, size=SIZE)
            total += len(listings)
            cont = len(listings) == SIZE
            utils.log(f"Total listing found: {total}.")
            time.sleep(2)  # Sleeping because I am not a robot

            contact_ids = set(
                models.Contact.objects.values_list("agency_id", flat=True)
            )
            listing_ids = set(models.Listing.objects.values_list("id", flat=True))

            for listing in listings:
                # Create contact
                listcontact = listing.get("contact")
                agency_id = listcontact.get("agencyId")

                if agency_id in contact_ids:
                    contact = models.Contact.objects.get(agency_id=agency_id)
                else:
                    contact = models.Contact.objects.create(
                        agency_id=listcontact.get("agencyId"),
                        agency_page=listcontact.get("agencyPage") or "",
                        contact_name=listcontact.get("contactName"),
                        img_url=listcontact.get("imgUrl") or "",
                        phone_number="".join(listcontact.get("phoneNumber").split()),
                        email=listcontact.get("email") == "true",
                        agency_link=listcontact.get("agencyLink") or "",
                    )
                contact_ids |= set([agency_id])

                # Create listing
                tags = listing.get("tags", [])
                listing_id = listing.get("id")

                room_qty = -1
                bedroom_qty = -1
                square_meter = -1
                floor = -1
                elevator_qty = 0

                for tag in tags:
                    if tag[-1] == "p":
                        room_qty = int(tag.split()[0])
                    if tag[-2:] == "ch":
                        bedroom_qty = int(tag.split()[0])
                    if tag[-2:] == "m²":
                        square_meter = int(float(tag.split()[0].replace(",", ".")))
                    if tag[-3:] == "etg":
                        floor = int(tag.split()[0])
                    if tag[-3:] == "asc":
                        elevator_qty = int(tag.split()[0])

                # Create listing
                if listing_id in listing_ids:
                    listing_object = models.Listing.objects.get(id=listing_id)
                else:
                    listing_object = models.Listing.objects.create(
                        id=listing_id,
                        room_qty=room_qty,
                        bedroom_qty=bedroom_qty,
                        floor=floor,
                        elevator_qty=elevator_qty,
                        square_meter=square_meter,
                        contact=contact,
                        publication_id=listing.get("publicationId"),
                        highlighting_level=listing.get("highlightingLevel"),
                        business_unit=listing.get("businessUnit"),
                        photos_qty=listing.get("photosQty", -1),
                        estate_type=ESTATE_TYPE(
                            listing.get("estateType") or "appartment"
                        ).name,
                        transaction_type=listing.get("transactionType"),
                        service_url=listing.get("serviceUrl"),
                        nature=listing.get("nature"),
                        is_exclusive=listing.get("isExclusive"),
                        city_label=listing.get("cityLabel"),
                        district_label=listing.get("districtLabel") or "",
                        zip_code=listing.get("zipCode"),
                        description=listing.get("description"),
                        video_url=listing.get("videoURL"),
                        virtual_visit_url=listing.get("virtualVisitURL"),
                        classified_url=listing.get("classifiedURL"),
                    )

                listing_ids |= set([listing_id])

                # Create pricing
                listpricing = listing.get("pricing")
                square_meter_price = int(
                    "0" + "".join(listpricing.get("squareMeterPrice").split()[:-1])
                )
                models.Pricing.objects.create(
                    listing=listing_object,
                    price=int(float(listpricing.get("rawPrice"))),
                    square_meter_price=square_meter_price,
                    monthly_price=listpricing.get("monthlyPrice"),
                    lifetime=listpricing.get("lifetime"),
                    loan_service_url=listpricing.get("loanServiceUrl"),
                )

                listphotos = listing.get("photos", [])
                for photo_url in listphotos:
                    models.Photo.objects.create(
                        listing=listing_object, photo_url=photo_url,
                    )

        utils.log(f"Finished polling listings ! Found {total} ✅")
