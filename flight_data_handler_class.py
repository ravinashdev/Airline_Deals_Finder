from config import settings
from api_class import API

class FlightDataHandler:
    def __init__(self):
        self.SHEETY_BEARER_TOKEN = settings.sheety.SHEETY_BEARER_TOKEN
    def retrieve_rows(self):
        api = API()
        SHEETY_BEARER_TOKEN = settings.sheety.SHEETY_BEARER_TOKEN
        api.get()