# Scrappe Gaumont API
import requests
from requests.exceptions import HTTPError
header = {'X-MAL-CLIENT-ID':'17710f15775c1c3e6bc63c28ec92c4b2'}
print('bordel')
def scrappe(url):
    try:
        response = requests.get(url,headers=header)
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        return jsonResponse

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')