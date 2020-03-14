import json
import requests

from utils import get_metadata, logs

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

if __name__ == "__main__":
    response = requests.post(url, headers=headers, data=data)
    res = json.loads(response.content)

    metadata = res.get("metadata")
    log(get_metadata(res))

