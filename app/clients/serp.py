# Adding a cache layer to limit daily requests
import requests
from requests import Response
class SerpClient:
    def __init__(self, http, settings):
        self.http = http
        self.api_key = settings.SERP_API_KEY
        self.base_url = settings.serp.base_url
    async def google_search(self, engine:str, **kwargs):
        # Define the required params for Google search
        # Will use enums and TypeDict later to enforce **kwargs since free tier allows 200 per month
        try:
            params = {
                "engine": engine,
                "api_key": self.api_key,
            }
            # Update params with additional (optional keyword arguments)
            params.update(kwargs)
            google_search_response = await self.http.get(
                self.base_url,
                params=params
            )
            google_search_response.raise_for_status()
            # print(f"Status Code: {google_search_response.status_code}")
            return google_search_response.json()
        except Exception as e:
            print(e)

