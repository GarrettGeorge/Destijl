from urllib.parse import urlparse
import json

import requests

import parsers.bonappetit as bonappetit
import parsers.allrecipes as allrecipes
import parsers.foodnetwork as foodnetwork
import parsers.themediterraneandish as themediterraneandish
import parsers.epicurious as epicurious
from .validate import urlScheme, supportedSite, ValidateError

def validateUrl(url):
    # Verify url passes all validators
    vs = [urlScheme, supportedSite]
    try:
        for validator in vs:
            valid = validator(url)
            if not valid:
                raise ValidateError("Failed to validate url, {}".format(url))
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
    elif domain == "allrecipes":
        data = allrecipes.parse(getHtml(url))
    elif domain == "foodnetwork":
        data = foodnetwork.parse(getHtml(url))
    elif domain == "themediterraneandish":
        data = themediterraneandish.parse(getHtml(url))
    elif domain == "epicurious":
        data = epicurious.parse(getHtml(url))

    print(json.dumps(data, indent=2, ensure_ascii=False))
    return data