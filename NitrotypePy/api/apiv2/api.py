from ..access import access
import json


def api(endpoint=""):
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
