from urllib.parse import urlparse
import json

import requests

import parsers.bonappetit as bonappetit
from .validate import urlScheme, supportedSite, ValidateError

def validateUrl(url):
    # Verify url passes all validators
    vs = [urlScheme, supportedSite]
    try:
        for validator in vs:
            valid = validator(url)
            if not valid:
                raise ValidateError("Failed to validate url!")
    except ValidateError as err:
        print("Error: {}".format(err))
        quit()
    except Exception as err:
        print("Error: Unknown error: {}".format(err))
        quit()

def getHtml(url):
    resp = requests.get(url)
    return resp.text

def getJson(url):
    validateUrl(url)

    domain = urlparse(url).netloc.split(".")[-2]
    
    if domain == "bonappetit":
        data = bonappetit.parse(getHtml(url))
    
    print(json.dumps(data, indent=2, ensure_ascii=False))