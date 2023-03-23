#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data = DataManager()
searcher = FlightSearch()

data.get_data()

sheet_data = data.data

need_update = False

for row in sheet_data:
    if row["iataCode"] == '':
        need_update = True
        code = searcher.find_iata_code(row['city'])
        row["iataCode"] = code

if need_update:
    print(sheet_data)
    data.data = sheet_data
    data.update_iata_codes()

