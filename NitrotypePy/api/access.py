try:
    import cloudscraper
except ModuleNotFoundError:
    raise ModuleNotFoundError("Unable to load cloudscraper")


def access(endpoint=""):
    """The function used to access the entirety of nitrotype.

    Endpoints: https://www.nitrotype.com/{endpoint}

    :param endpoint: The end url to access.
    :type endpoint: str
    :returns: A string of the html of the webpage, or of a json from the api.
    :rtype: str
    """

    base_url = "https://www.nitrotype.com/"
    scraper = None
    try:
        scraper = cloudscraper.create_scraper()
    except:
        scraper = cloudscraper.CloudScraper()
    finally:
        if scraper:
            return scraper.get(base_url + endpoint).text

    return False
