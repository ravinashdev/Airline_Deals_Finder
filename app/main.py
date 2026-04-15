# ---------------------------- IMPORTS ------------------------------- #
import asyncio
from core.config import settings
from core.http import HTTPClient
import datetime as dt
# Import All Clients Classes
from clients.sheety import SheetyClient
from clients.twillio import Twillio

# Used to return a printed report for Dynaconf for debugging
# from dynaconf import inspect_settings
# inspect_settings(settings, print_report=True)
# ---------------------------- CONSTANTS ------------------------------- #
# Define clients with args for API calls
now = dt.datetime.now().strftime("%m-%d-%Y" "%H:%M:%S")
http = HTTPClient()
sheety = SheetyClient(http, settings)
twillio = Twillio()

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
async def main():

    # Data Grabber (Sheety)
    sheety_response = await sheety.get_rows()
    print(sheety_response)
    # Flight Finder (Serp)

    # Message Sender(Twillio)
    message =f"Hello this a Test {now}"
    to="+13478579787"
    twillio_response = twillio.send_text(message, to)
    print(twillio_response)
asyncio.run(main())
# print(settings.SHEETY_BEARER_TOKEN)
# print(settings.sheety.base_url)
