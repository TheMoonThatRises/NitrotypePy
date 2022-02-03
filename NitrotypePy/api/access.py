import cloudscraper


def access(endpoint=''):
    base_url = 'https://www.nitrotype.com/'
    scraper = None
    try:
        scraper = cloudscraper.create_scraper()
    except:
        scraper = cloudscraper.CloudScraper()
    finally:
        if scraper:
            return scraper.get(base_url + endpoint).text
        else:
            print('Unable to get cloudscraper.')
            raise
