import requests
import os
from dotenv import load_dotenv

tequila_endpoint = "https://api.tequila.kiwi.com"

load_dotenv("C:/Users/huang/PycharmProjects/EnvironmentVariables/.env")

API_KEY = os.getenv("TEQUILA_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        pass

    def find_iata_code(self, city):
        print(city)
        # location_endpoint = f"{tequila_endpoint}/locations/query"
        location_endpoint=f"https://api.tequila.kiwi.com/locations/query?term={city}&locale=en-US&location_types=city&limit=10&active_only=true"
        headers = {"apiKey": API_KEY}
        # query = {"term": city, "location_types": "airport"},
        response = requests.get(url=location_endpoint, headers=headers)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
