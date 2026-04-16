
class DataCleaner:
    def __init__(self):
        pass
    def clean_google_flight_data(self, google_response_data):
        best_flights_list = google_response_data["best_flights"]
        flight_info_list = []
        flight_info_message_list = []
        for flight in best_flights_list:
            flight_info = {
                "Leg_1": flight["flights"][0],
                "Leg_2": flight["flights"][1],
                "Layover": flight["layovers"],
                "Duration": f"{divmod(flight["total_duration"], 60)[0]:2d} hours & {divmod(flight["total_duration"], 60)[1]:2d} minutes",
                "Type": flight["type"].title(),
                "Price": flight["price"]
            }
            flight_info_list.append(flight_info)
            flight_info_message = f"""
            Leaving From: {flight_info["Leg_1"]["departure_airport"]["name"]}
            Leg 1:
            ({flight_info["Leg_1"]["departure_airport"]["id"]} -> {flight_info["Leg_1"]["arrival_airport"]["id"]}) 
            Departing: {flight_info["Leg_1"]["departure_airport"]["time"]} 
            Arriving: {flight_info["Leg_1"]["arrival_airport"]["time"]} Local Time
            
            Layover: 
            In: {flight_info["Layover"][0]["name"]}
            For:{divmod(flight_info["Layover"][0]["duration"], 60)[0]:2d} hours & {divmod(flight_info["Layover"][0]["duration"], 60)[1]:2d} minutes
           
            Leg 2:
            ({flight_info["Leg_2"]["departure_airport"]["id"]} -> {flight_info["Leg_2"]["arrival_airport"]["id"]}) 
            Departing: {flight_info["Leg_2"]["departure_airport"]["time"]} 
            Arriving: {flight_info["Leg_2"]["arrival_airport"]["time"]} Local Time
            
            Total Travel Time: {flight_info["Duration"]}
            {flight_info["Type"]} Price: ${flight_info["Price"]} USD
            
            """
            flight_info_message_list.append(flight_info_message)
        return flight_info_message_list

# with open('../../google_response_data.json') as json_file:
#     google_response_data = json.load(json_file)
# print(clean_google_flight_data(google_response_data))


