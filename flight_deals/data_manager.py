import os
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT_GET = os.environ["SHEETY_ENDPOINT_GET"]
        self.SHEETY_ENDPOINT_POST = os.environ["SHEETY_ENDPOINT_POST"]
        self.SHEETY_ENDPOINT_PUT = os.environ["SHEETY_ENDPOINT_PUT"]
        self.USER = os.environ["USER"]
        self.PASSWORD = os.environ["PASSWORD"]
        self.sheet = {}

    def get_request(self):
        response = requests.get(url=self.SHEETY_ENDPOINT_GET, auth=(self.USER, self.PASSWORD))
        self.sheet = response.json()["prices"]
        return self.sheet

    def put_request(self):
        for city in self.sheet:
            prices = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response2 = requests.put(url=f"{self.SHEETY_ENDPOINT_PUT}/{city['id']}", auth=(self.USER, self.PASSWORD), json=prices)
            # print(response)


    def put_price(self):
        for city in self.sheet:
            prices = {
                "price": {
                    "Actual": city["Actual"]
                }
            }
            response2 = requests.put(url=f"{self.SHEETY_ENDPOINT_PUT}/{city['id']}", auth=(self.USER, self.PASSWORD),
                                     json=prices)