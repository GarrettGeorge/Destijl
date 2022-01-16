import validators
from urllib.parse import urlparse

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValidateError(Error):
# Raised when url fails to validate for any reason
    pass

def urlScheme(url):
    return validators.url(url)

supported_sites = [
    "bonappetit",
    "allrecipes",
    "foodnetwork",
    "themediterraneandish",
    "epicurious"
]

def supportedSite(url):
    if not urlparse(url).netloc.split(".")[-2] in supported_sites:
        raise ValidateError("Url is not in list of supported sites: {}".format(",".join(supported_sites))) 
    return True
