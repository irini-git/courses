import datetime
import requests
import os

# --------------- Constants ---------------
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
TOMORROW = tomorrow.strftime('%d/%m/%Y')
DATE_TO = '25/01/2023'  # hard coded as relative delta is not callable
CURRENCY = 'GBP'
FLY_FROM = 'LON'

tequila_api = os.environ.get('TEQUILA_API_KEY')
tequila_endpoint = 'https://api.tequila.kiwi.com'
tequila_search_endpoint = f'{tequila_endpoint}/v2/search'
tequila_location_endpoint = f'{tequila_endpoint}/locations/query'


flight_headers = {
    'apikey': tequila_api
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self, prices):
        self.prices = prices
        self.search_offer()

    def search_offer(self):

        for price in self.prices:

            location_search = {
                'term': price['city'],
                'location_types': 'city',
                'limit': 1
            }

            tequila_request = requests.get(url=tequila_location_endpoint, params=location_search,
                                           headers=flight_headers)
            data = tequila_request.json()
            # update iataCode
            # could post to sheets via API, but have a limited number of requests
            price['iataCode'] = data['locations'][0]['code']

            flight_search = {
                'fly_from': FLY_FROM,
                'fly_to': price['iataCode'],
                'date_from': TOMORROW,
                'date_to': DATE_TO,
                'price_to': price['lowestPrice'],
                'max_stopovers': 0,
                'flight_type': 'round',
                'nights_in_dst_from': 6, # optionally prompt from user input
                'nights_in_dst_to': 27, # optionally prompt from user input
                'curr': CURRENCY,
                'limit': 1
            }

            tequila_request = requests.get(url=tequila_search_endpoint, params=flight_search, headers=flight_headers)
            search_results = tequila_request.json()

            if not search_results['data']:
                price['offer'] = 'none'
                price['city_from'] = 'none'
                price['airport_from'] = 'none'
                price['city_to'] = 'none'
                price['airport_to'] = 'none'
                price['departure'] = 'none'
                price['arrival'] = 'none'

            else:
                price['offer'] = search_results['data'][0]['price']
                price['city_from'] = search_results['data'][0]['cityFrom']
                price['airport_from'] = search_results['data'][0]['flyFrom']
                price['city_to'] = search_results['data'][0]['cityTo']
                price['airport_to'] = search_results['data'][0]['flyTo']
                price['departure'] = search_results['data'][0]['route'][0]['local_departure'].split('T')[0]
                price['arrival'] = search_results['data'][0]['route'][1]['local_departure'].split('T')[0]
