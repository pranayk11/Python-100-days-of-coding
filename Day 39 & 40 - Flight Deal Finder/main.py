# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "LON"
# print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_month_from_today = (datetime.now() + timedelta(days=(6*30))).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = flight_search.check_fights(
        ORIGIN_CITY_IATA, destination["iataCode"], from_time=tomorrow, to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        message = (f"Low price alert! Only {flight.price} pounds to fly from"
                                       f"{flight.origin_city}-{flight.origin_airport} to "
                                       f"{flight.destination_city}-{flight.destination_airport}, from "
                                       f"{flight.out_date} to {flight.return_date}")

        if flight.stop_over > 0:
            message += f"\nFlight has {flight.stop_over} stop over, via {flight.via_city}."
            print(message)

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
               f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_mail(message, link)


