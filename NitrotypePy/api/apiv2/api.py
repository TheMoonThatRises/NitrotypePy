from ..access import access
import json

def api(endpoint = ''):
    data = json.loads(access('api/v2/' + endpoint))

    if data['status'] == 'OK':
        return data['results']
    else:
        print(data['status'])
        print(data['results']['message'])
        raise
