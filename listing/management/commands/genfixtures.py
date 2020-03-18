import parser.utils as utils

from django.core.management.base import BaseCommand

from listing.management.commands.__fixture__.response import MOCK_RESPONSE
import listing.models as models


class Command(BaseCommand):
    help = "Some useful objects to start using immo in dev."

    def handle(self, *args, **options):
        models.Pricing.objects.all().delete()
        models.Listing.objects.all().delete()
        models.Contact.objects.all().delete()

        listings = utils.get_listings_from_response(MOCK_RESPONSE)

        contact_ids = set()
        listing_ids = set()

        for listing in listings:

            # Create contact
            listcontact = listing.get("contact")
            agency_id = listcontact.get("agencyId")

            if agency_id in contact_ids:
                contact = models.Contact.objects.get(agency_id=agency_id)
            else:
                contact = models.Contact.objects.create(
                    agency_id=listcontact.get("agencyId"),
                    agency_page=listcontact.get("agencyPage"),
                    contact_name=listcontact.get("contactName"),
                    img_url=listcontact.get("imgUrl"),
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
                    estate_type=listing.get("estateType"),
                    transaction_type=listing.get("transactionType"),
                    service_url=listing.get("serviceUrl"),
                    nature=listing.get("nature"),
                    is_exlusive=listing.get("isExlusive"),
                    city_label=listing.get("cityLabel"),
                    district_label=listing.get("districtLabel") or "",
                    zip_code=listing.get("zipCode"),
                    description=listing.get("description"),
                    video_url=listing.get("videoUrl"),
                    virtual_visit_url=listing.get("virtualVisitUrl"),
                    classified_url=listing.get("classifiedUrl"),
                )

            listing_ids |= set([listing_id])

            # Create pricing
            listpricing = listing.get("pricing")
            square_meter_price = int(
                "".join(listpricing.get("squareMeterPrice").split()[:-1])
            )
            models.Pricing.objects.create(
                listing=listing_object,
                price=int(float(listpricing.get("rawPrice"))),
                square_meter_price=square_meter_price,
                monthly_price=listpricing.get("monthlyPrice"),
                lifetime=listpricing.get("lifetime"),
                loan_service_url=listpricing.get("loanServiceUrl"),
            )

            # Create photos
            # "https://v.seloger.com/s/width/400/visuels/1/8/g/m/18gmwaa0mrc089r86m0ktofrpxrudcuozkqw9tu1g.jpg",
            # "https://v.seloger.com/s/width/400/visuels/1/e/5/c/1e5cni6b1ql7hgfhfyj5zu0enh81qo8cck0bjqq8k.jpg",
            # "https://v.seloger.com/s/width/400/visuels/0/v/1/l/0v1l7mk26s1yx4rdiauuu1gbhglfsk78v6s38nmms.jpg",
            # "https://v.seloger.com/s/width/400/visuels/0/w/u/b/0wubh3b27bnyo4zatra63xvh9iv1igd5irm4ijot0.jpg",
            # "https://v.seloger.com/s/width/400/visuels/1/u/e/o/1ueolk16bzfd1r8dmmuv779oyx6ldd9q4c6mfh104.jpg",
