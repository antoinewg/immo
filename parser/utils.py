import json
import requests

from .constants import FILTERS_NAME_VALUE, FILTERS_MIN_MAX


def log(string):
    """all outputs are centralized in this function, if we later want to show time/use a logger."""
    print(string)


def get_metadata(response):
    metadata = response.get("metadata")
    search = metadata.get("search")
    res = f"\nFetched {search.get('nbresults')} results in {' > '.join(metadata.get('summary'))}.\n"

    # Display which filters where selected (yes/no type)
    for category in FILTERS_NAME_VALUE:
        active = [el.get("name") for el in search.get(category, {}) if el.get("value")]
        if len(active) > 0:
            res += f"\t- {category}: {', '.join(active)}\n"

    # Display the "range" filters
    for category in FILTERS_MIN_MAX:
        mini, maxi = (
            search.get(category, {}).get("min"),
            search.get(category, {}).get("max"),
        )
        if mini or maxi:
            res += f"\t- {category}: [{mini if mini else ''}, {maxi if maxi else ''}]\n"

    return res


def get_listings_from_response(response):
    return response.get("classifiedsData").get("classifieds")


def fetch_batch_listing(start=0, size=25):
    url = f"https://www.seloger.com/list/api/externaldata?from={start}&size={size}&isSeo=false"

    headers = {
        "authority": "www.seloger.com",
        "accept": "application/json",
        "sec-fetch-dest": "empty",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "content-type": "application/json",
        "origin": "https://www.seloger.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "referer": "https://www.seloger.com/list.htm?projects=2%2C5&types=2%2C1&natures=1%2C2%2C4&places=%5B%7Bcp%3A75%7D%5D&enterprise=0&qsVersion=1.0&LISTING-LISTpg=2",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,th;q=0.6,pl;q=0.5,es;q=0.4",
    }

    data = '{"enterprise":false,"projects":[2,5],"types":[1,2],"places":[{"label":"Paris","dpCode":["75"]}],"natures":[1,2,4]}'

    response = json.loads(requests.post(url, headers=headers, data=data).content)
    listings = get_listings_from_response(response)
    return listings
