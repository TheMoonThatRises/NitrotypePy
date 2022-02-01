from ...apiv2 import api

def news(news_id = 0):
    if news_id:
        return api.api('news/' + news_id)
    else:
        return api.api('news')
