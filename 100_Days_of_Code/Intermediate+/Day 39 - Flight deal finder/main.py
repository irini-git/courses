import os
import json
import datetime
from data_manager import DataManager
from flight_search import FlightSearch
import pprint

# This file will need to use the DataManager,
# FlightSearch,
# FlightData,
# NotificationManager classes to achieve the program requirements.

# ----------- Constants -------------

tequila_api = os.environ.get('TEQUILA_API_KEY')
tequila_endpoint = 'https://api.tequila.kiwi.com'
tequila_search_endpoint = f'{tequila_endpoint}/v2/search'
tequila_location_endpoint = f'{tequila_endpoint}/locations/query'

# tequila_password = os.environ.get('TEQUILA_PASS')
# tequila_first_name = os.environ.get('TEQUILA_FIRST_NAME')  # 'First name' and 'Last name'
# tequila_lastname_name = os.environ.get('TEQUILA_LAST_NAME')

FILENAME = 'data/prices.json'


# ---------------- Load data ----------------
data_manager = DataManager(FILENAME)
prices = data_manager.prices['prices']

flight_search = FlightSearch(prices)

# ---------------- Offer ----------------
for price in flight_search.prices:
    if price["offer"] != 'none':
        message = f'Low price alert! Only £{price["offer"]} to fly from {price["city_from"]}-{price["airport_from"]} to {price["city_to"]}-{price["airport_to"]}, from {price["departure"]} to {price["arrival"]}.'
        print(message)

        # instead of printing could send SMS via twilio
        # not performed

# ---------------- Send message ----------------




