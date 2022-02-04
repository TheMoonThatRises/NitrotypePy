from ...access import access
import json


def bootstrap(item=""):
    bootstrap_items = json.loads(access("index/624/bootstrap.js")[40:-15])

    for bootstrap_item in bootstrap_items:
        if bootstrap_item[0].lower() == item.lower():
            return bootstrap_item[1]

    return False
