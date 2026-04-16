# ---------------------------- IMPORTS ------------------------------- #
import asyncio
import pandas as pd
import time
import json
from app.clients.data_cleaner import DataCleaner
from core.config import settings
from core.http import HTTPClient
import datetime as dt
from datetime import timedelta
# Import All Clients Classes
from clients.sheety import SheetyClient
from clients.twillio import Twillio
from clients.serp import SerpClient

# Used to return a printed report for Dynaconf for debugging
# from dynaconf import inspect_settings
# inspect_settings(settings, print_report=True)
# ---------------------------- CONSTANTS ------------------------------- #
# Define clients with args for API calls
now = dt.datetime.now().strftime("%m-%d-%Y" "%H:%M:%S")
today = dt.datetime.today()
one_week_from_today = (today + timedelta(days=7))
one_week_from_today_formatted = one_week_from_today.strftime("%Y-%m-%d")
six_months_from_today = (today + timedelta(days=183))
six_months_from_today_formatted = six_months_from_today.strftime("%Y-%m-%d")
four_weeks_from_departure_day = (six_months_from_today + timedelta(days=28))
four_weeks_from_departure_day_formatted = four_weeks_from_departure_day.strftime("%Y-%m-%d")

http = HTTPClient()
sheety = SheetyClient(http, settings)
google = SerpClient(http, settings)
data_cleaner = DataCleaner()
twillio = Twillio()
# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #
async def main():
    # ------------------------------Data Grabber (Sheety)-------------------------------
    sheety_response = await sheety.get_rows()
    sheety_dataframe = pd.DataFrame(sheety_response["prices"])
    sheety_dataframe_reordered = sheety_dataframe[['iataCode','lowestPrice','id', 'city']]
    sheety_dataframe_row_1 = sheety_dataframe_reordered.iloc[1]
    # for rows in sheety_dataframe_reordered.itertuples():
    #     print(rows)
    iataCode = sheety_dataframe_row_1["iataCode"]
    # print(iataCode)

    #------------------------------- Flight Finder (Serp)-------------------------------
    engine="google_flights"
    google_response = await google.google_search(
        engine,
        arrival_id=iataCode,
        departure_id="JFK",
        currency="USD",
        type="1",
        stops="2",
        outbound_date=six_months_from_today_formatted,
        return_date=four_weeks_from_departure_day_formatted
    )
    # print(google_response)
    cleaned_google_response_data = data_cleaner.clean_google_flight_data(google_response)
    # print(cleaned_google_response_data)

    # -------------------------------Message Sender(Twillio)-------------------------------
    message = cleaned_google_response_data[0]
    to="+13478579787"
    twillio_response = twillio.send_text(message, to)
    print(twillio_response)
# ---------------------------- UI SETUP ------------------------------- #
asyncio.run(main())

