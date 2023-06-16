import os
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_iataCode(self, location):
        API_KEY = os.environ['API_KEY']
        ENDPOINT = os.environ['TEQUILA_ENDPOINT']
        headers = {
            "apikey": API_KEY,
        }
        parameters = {
            "term": location,
            "location_types": "city"
        }
        response = requests.get(url=ENDPOINT, headers=headers, params=parameters)
        return response.json()["locations"][0]["code"]
