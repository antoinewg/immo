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
        active = [el.get("name") for el in search.get(category) if el.get("value")]
        if len(active):
            res += f"\t- {category}: {', '.join(active)}\n"

    # Display the "range" filters
    for category in FILTERS_MIN_MAX:
        mini, maxi = search.get(category).get("min"), search.get(category).get("max")
        if mini or maxi:
            res += f"\t- {category}: [{mini if mini else ''}, {maxi if maxi else ''}]\n"

    return res
