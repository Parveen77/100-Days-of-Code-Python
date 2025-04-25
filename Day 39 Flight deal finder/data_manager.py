import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth


load_dotenv()  # Load variables from .env into the environment

sheety_endpoint= "https://api.sheety.co/ee58af7e3286940458d54e3198bc1d71/flightDeals/prices"

class DataManager:
    def __init__(self):
        self._user = os.environ["USERNAME_SHEETY"]
        self._password = os.environ["PASSWORD_SHEETY"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        
    def get_destination_data(self):
        response = requests.get(sheety_endpoint, auth = self._authorization)
        response.raise_for_status()
        result = response.json()
        self.destination_data = result["prices"]
        return self.destination_data
    
    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            #print(response.text)


    




    