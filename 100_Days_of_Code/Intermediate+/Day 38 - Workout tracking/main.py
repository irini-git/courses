import requests
from datetime import datetime
import os

# attribution to Nutritionix

# ---------------- Constants ---------------
app_id = os.environ.get('APP_ID')
api_key = os.environ.get('API_KEY')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get('SHEET_ENDPOINT')
sheet_user = os.environ.get('SHEET_USER')
sheet_pass = os.environ.get('SHEET_PASS')

GENDER = 'female'

# Basic Authentication
basic = requests.auth.HTTPBasicAuth(sheet_user, sheet_pass)

exercise_text = input("Tell me which exercises you did: ")

headers = {
     'x-app-id': app_id,
     'x-app-key': api_key
 }

parameters = {
     "query": exercise_text
 }

today = datetime.now()
DATE = today.strftime("%d/%m/%Y")
TIME = today.strftime("%H:%M:%S")

# ---------------- Post exercise ----------------
exercise_response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = exercise_response.json()


for item in result['exercises']:
    workout_data = {
        'workout': {
            'date': DATE,
            'time': TIME,
            'exercise': item['user_input'].title(),
            'duration': item['duration_min'],
            'calories': item['nf_calories']
        }
}


    # sheet
    for data in workout_data:
        sheet_response = requests.post(url=sheet_endpoint, json=workout_data, auth=basic)
        print("response.status_code =", sheet_response.status_code)
        print("response.text =", sheet_response.text)

