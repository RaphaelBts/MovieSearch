# Scrappe Gaumont API
import requests
from requests.exceptions import HTTPError

URL = 'https://www.cinemaspathegaumont.com/api/show/uncharted/showtimes/cinema-pathe-dammarie'

def scrappe(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        return jsonResponse

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

res = scrappe(URL)
print(res)