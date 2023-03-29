#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data = DataManager()
searcher = FlightSearch()
notification_manager = NotificationManager()

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

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = searcher.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight and flight.price < destination["lowestPrice"]:
        notification_manager.send_message(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )