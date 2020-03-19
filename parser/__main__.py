import json
import requests

from .utils import get_listings_from_response, get_metadata, log

url = "https://www.seloger.com/list/api/externaldata?from=0&size=25&isSeo=false"

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

log(get_metadata(response))

log(len(get_listings_from_response(response)))
