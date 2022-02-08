from ..access import access
import json


def api(endpoint=""):
    """Access the nitrotype api.

    Endpoint
    --------
        https://www.nitrotype.com/api/v2/{endpoint}

    Parameters
    ----------
    endpoint: str
        The endpoint for the nitrotype api.

    Returns
    -------
    dict
        A dict of the information.
    """

    try:
        data = json.loads(access("api/v2/" + str(endpoint)))
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
