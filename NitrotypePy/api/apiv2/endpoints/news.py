from typing import List, Union
from ...apiv2.api import api
from ....objects.api.apiv2.endpoints.news import News


def news(news_id=0) -> Union[News, List[News]]:
    if news_id:
        return api('news/' + news_id)
    else:
        return api('news')
