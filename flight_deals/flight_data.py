import requests
import os
from datetime import datetime, timedelta

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = 0
        self.departure_airport_code = 'LON'
        self.departure_city = 'London'
        self.TEQUILA_ENDPOINT_SEARCH = "https://api.tequila.kiwi.com/v2/search"


    def search_flight(self, row):

        localization = row["iataCode"]
        # print(localization)
        API_KEY = os.environ['API_KEY']

        tomorrow = datetime.today() + timedelta(days=1)
        last_day = tomorrow + timedelta(days=30 * 6)
        headers = {
            "apikey": API_KEY,
        }
        parameters = {
            "fly_from": f"city:{self.departure_airport_code}",
            "fly_to": localization,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": last_day.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "adults": 1,
            "one_for_city": 1,
        }
        response = requests.get(url=self.TEQUILA_ENDPOINT_SEARCH, headers=headers, params=parameters)
        return response.json()["data"][0]["price"]
