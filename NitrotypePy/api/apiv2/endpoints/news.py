from typing import List, Union
from ...apiv2.api import api
from ....objects.api.apiv2.endpoints.news import News


def news(news_id=0) -> Union[News, List[News]]:
    """Returns all of the latest nitrotype's latest news or the specific news.

    If news_id is specified, then it will return that specific news.

    Endpoint
    --------
        https://www.nitrotype.com/api/v2/news/<news_id>

    Parameter
    ---------
    news_id : int
        The id of the news.

    Returns
    -------
    dict
        A dict of the latest news, or a single news dict.
    """

    if news_id:
        return api("news/" + str(news_id))
    else:
        return api("news")
