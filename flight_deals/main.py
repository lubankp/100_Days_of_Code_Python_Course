#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to
# achieve the program requirements.

from pprint import pprint
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from flight_search import FlightSearch
import requests

data_Manager = DataManager()
sheet_data = data_Manager.get_request()
pprint(sheet_data)

flight_Search = FlightSearch()

if sheet_data[0]["iataCode"] == '':
    for row in sheet_data:
        row["iataCode"] = flight_Search.get_iataCode(row["city"])
    data_Manager.sheet = sheet_data
    data_Manager.put_request()

flight_Data = FlightData()
for row in data_Manager.sheet:
    row["Actual"] = flight_Data.search_flight(row)

data_Manager.put_price()
