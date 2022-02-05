from ..access import access
import json


def api(endpoint=""):
    """Access the nitrotype api.

    Endpoint: https://www.nitrotype.com/api/v2/{endpoint}

    :param endpoint: The endpoint for the nitrotype api.
    :type endpoint: str
    :returns: A dict of the information.
    :rtype: dict
    """

    try:
        data = json.loads(access("api/v2/" + endpoint))
    except Exception as e:
        print("Unable to access api endpoint.")
        print(e)
        return False

    if data["status"] == "OK":
        return data["results"]
    else:
        print(data["status"])
        print(data["results"]["message"])
        return False
