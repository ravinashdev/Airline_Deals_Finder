# ---------------------------- IMPORTS ------------------------------- #
import asyncio
from api_class import API


# ---------------------------- CONSTANTS ------------------------------- #

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #
async def main():
    async with API() as api:
        data = await api.get("https://example.com")
        print(data)
# ---------------------------- UI SETUP ------------------------------- #
# Run all API calls
asyncio.run(main())