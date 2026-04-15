# Adding a cache layer to limit daily requests
import requests
from requests import Response
class SheetyClient:
    def __init__(self, http, settings):
        self.http = http
        self.base_url = settings.sheety.base_url
        self.api_key = settings.SHEETY_BEARER_TOKEN
    # Name methods based on what it does in API
    async def get_rows(self):
        try:
            get_rows_reponse = await self.http.get(
                self.base_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}"
                }
            )
            return get_rows_reponse.json()
        except Exception as e:
            print(e)
