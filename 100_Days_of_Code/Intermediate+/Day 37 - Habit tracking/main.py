import requests
from datetime import datetime
import os

# -------------- Constants --------------

# Environment variables
userName = os.environ.get('USERNAME')
graphId = os.environ.get('GRAPH_ID')

GRAPH_NAME = 'Cycling Graph'
GRAPH_UNIT = 'Km'
GRAPH_TYPE = 'float'
GRAPH_COLOR = 'shibafu'

# QUANTITY = '2'
# today = datetime.now()
today = datetime(year=2022, month=9, day=19)
TODAY = today.strftime("%Y%m%d")

pixela_endpoint = 'https://pixe.la/v1/users'
#TOKEN = # get TOKEN from pixela
graph_endpoint = f'{pixela_endpoint}/{userName}/graphs'
pixel_creation_endpoint = f'{pixela_endpoint}/{userName}/graphs/{graphId}'
pixel_update_endpoint = f'{pixela_endpoint}/{userName}/graphs/{graphId}/{TODAY}'

user_params = {
    'token' : TOKEN,
    'username' : userName,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

graph_config = {
    'id' : graphId,
    'name' : GRAPH_NAME,
    'unit' : GRAPH_UNIT,
    'type' : GRAPH_TYPE,
    'color' : GRAPH_COLOR
}

QUANTITY = input('How many km did you cycle today?')
update_data = {'quantity' : QUANTITY}

pixel_data = {
    'date' : TODAY,
    'quantity' : QUANTITY
}

headers = {
    'X-USER-TOKEN' : TOKEN
}

# -------------- Create graph --------------

# Pixela
# 1. Create your user account
# Call /v1/users API by HTTP POST.
# only run once
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# 2. Create a graph definition
# Comment once done
# Call /v1/users/<username>/graphs by HTTP POST.
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# 3. Get the graph!
# This is also /v1/users/<username>/graphs/<graphID> API.

# 4. Post value to the graph
# Call /v1/users/<username>/graphs/<graphID> by HTTP POST.
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# 5. Update the pixel
# Update the quantity already registered as a "Pixel".
# response = requests.put(url=pixel_update_endpoint, json=update_data, headers=headers)
# print(response.text)

# 6. Delete the pixel
# Delete the registered "Pixel".
# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)