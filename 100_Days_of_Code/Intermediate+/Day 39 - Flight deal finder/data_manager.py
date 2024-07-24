import json
# import os

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, filename):
        # load data from Sheet via API
        # will be using hard-cosing as limited in number of requests
        # self.sheet_endpoint = os.environ.get('SHEET_ENDPOINT')
        # self.sheet_user = os.environ.get('SHEET_USER')
        # self.sheet_pass = os.environ.get('SHEET_PASS')
        # Basic Authentication
        # basic = requests.auth.HTTPBasicAuth(sheet_user, sheet_pass)

        # sheet_response = requests.get(url=sheet_endpoint, auth=basic)
        # print("response.status_code =", sheet_response.status_code)
        # print("response.text =", sheet_response.text)
        # self.prices_json = sheet_response.text

        # load from json
        # try loading from sheets, if not working, load from json

        with open(filename) as f:
            self.prices = json.load(f)
