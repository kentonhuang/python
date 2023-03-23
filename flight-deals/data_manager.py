import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/huang/PycharmProjects/EnvironmentVariables/.env")

bearer = os.getenv("SHEETY_FLIGHT_BEARER")

sheety_url = "https://api.sheety.co/ddfbe74a1b2f5e352aba3c577a4c8d42/copyOfFlightDeals/prices"
sheety_header = {
    "Authorization": f"Bearer {bearer}"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.data = []
        pass

    def get_data(self):

        sheety_response = requests.get(sheety_url, headers=sheety_header)
        self.data = sheety_response.json()["prices"]

        return self.data

    def update_iata_codes(self):

        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{sheety_url}/{city['id']}",
                headers=sheety_header,
                json=new_data
            )
            print(response.text)
