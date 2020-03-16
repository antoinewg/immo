import json
import requests

from .utils import extract_advertisement, get_metadata, log

url = "https://www.seloger.com/list/api/externaldata"

headers = {
    "authority": "www.seloger.com",
    "accept": "application/json",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "content-type": "application/json",
    "origin": "https://www.seloger.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "referer": "https://www.seloger.com/list.htm?projects=2,5&types=1,2&natures=1,2,4&places=[{cp:75}]&enterprise=0&qsVersion=1.0",
    "accept-language": "fr-FR,fr;q=0.9",
}

data = '{"enterprise":false,"projects":[2,5],"types":[1,2],"places":[{"label":"Paris","dpCode":["75"]}],"natures":[1,2,4]}'

response = json.loads(requests.post(url, headers=headers, data=data).content)

log(get_metadata(response))

df = extract_advertisement(response)
