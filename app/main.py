# ---------------------------- IMPORTS ------------------------------- #
import asyncio
from core.config import settings
from core.http import HTTPClient
# Import All Clients Classes
from clients.sheety import SheetyClient
# Used to return a printed report for Dynaconf for debugging
# from dynaconf import inspect_settings
# inspect_settings(settings, print_report=True)
# ---------------------------- CONSTANTS ------------------------------- #
# Define clients with args for API calls
http = HTTPClient()
sheety = SheetyClient(http, settings)

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
async def main():
    sheety_response = await sheety.get_rows()
    print(sheety_response)
asyncio.run(main())
# print(settings.SHEETY_BEARER_TOKEN)
# print(settings.sheety.base_url)
