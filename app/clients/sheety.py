class SheetyClient:
    def __init__(self, http, settings):
        self.http = http
        self.base_url = settings.sheety.base_url
        self.api_key = settings.SHEETY_BEARER_TOKEN
    async def get_rows(self):
        get_rows_reponse = await self.http.get(
            self.base_url,
            headers={
                "Authorization": f"Bearer {self.api_key}"
            }
        )
        return get_rows_reponse.json()