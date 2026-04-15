# ---------------------------- IMPORTS ------------------------------- #
import asyncio
import pandas as pd
from core.config import settings
from core.http import HTTPClient
import datetime as dt
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
http = HTTPClient()
sheety = SheetyClient(http, settings)
google = SerpClient(http, settings)
twillio = Twillio()
# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
async def main():
    # Data Grabber (Sheety)
    sheety_response = await sheety.get_rows()
    sheety_dataframe = pd.DataFrame(sheety_response["prices"])
    sheety_dataframe_reordered = sheety_dataframe[['iataCode','lowestPrice','id', 'city']]

    print(sheety_response)
    print(sheety_dataframe_reordered)
    # Flight Finder (Serp)
    engine="google_flights"
    # google_response = await google.google_search(engine)
    # print(google_response)
    # Message Sender(Twillio)
    # message =f"Hello this a Test {now}"
    # to="+13478579787"
    # twillio_response = twillio.send_text(message, to)
    # print(twillio_response)
asyncio.run(main())
# print(settings.SHEETY_BEARER_TOKEN)
# print(settings.sheety.base_url)
