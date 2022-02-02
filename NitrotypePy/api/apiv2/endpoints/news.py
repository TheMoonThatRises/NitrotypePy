from ...apiv2.api import api

def news(news_id = 0):
    if news_id:
        return api('news/' + news_id)
    else:
        return api('news')
