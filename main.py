# ---------------------------- IMPORTS ------------------------------- #
import asyncio
from config import settings
from api_class import API


# ---------------------------- CONSTANTS ------------------------------- #
SHEETY_BEARER_TOKEN = settings.sheety.SHEETY_BEARER_TOKEN
SERP_API_KEY = settings.serp.SERP_API_KEY
TWILLIO_TEST_ACCOUNT_SID = settings.twillio.TWILLIO_TEST_ACCOUNT_SID
TWILLIO_TEST_AUTH_TOKEN = settings.twillio.TWILLIO_TEST_AUTH_TOKEN
# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #
async def main():
    async with API() as api:
        data = await api.get("https://example.com")
        print(data)
# ---------------------------- UI SETUP ------------------------------- #
# Run all API calls
# asyncio.run(main())
print(SHEETY_BEARER_TOKEN)
print(SERP_API_KEY)
print(TWILLIO_TEST_ACCOUNT_SID)
print(TWILLIO_TEST_AUTH_TOKEN)