import time
from datetime import datetime, timedelta 
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()


# Set your origin airport New Delhi 
ORIGIN_CITY_IATA = "DEL"

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if sheet_data[0]["iataCode"] == "":
        row["iataCode"] = FlightSearch.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2) 
        
#print(f"sheet_data:\n {sheet_data}")

#Very slow response (use only when there is updation of IATA code is required)
#data_manager.destination_data = sheet_data
#data_manager.update_destination_data()

# ==================== Search for Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(20))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.get_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    
    
    cheapest_flight = FlightData.find_cheapest_flight(flights)
    print(f"{destination['city']}: ₹{cheapest_flight.price} on {cheapest_flight.out_date} and return date {cheapest_flight.return_date}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)


#TODO Update the flight deals sheet with cheapest price to thier 