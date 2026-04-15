# ---------------------------- IMPORTS ------------------------------- #
from app.core.config import settings
# Twillio
from twilio.rest import Client
# ---------------------------- FUNCTIONS ------------------------------- #
class Twillio:
    def __init__(self):
        self.sid = settings.TWILLIO_TEST_ACCOUNT_SID
        self.key = settings.TWILLIO_TEST_AUTH_TOKEN
        self.from_="+18559411028"
        self.client = Client(self.sid, self.key)
    def send_text(self, body, to):
        try:
            text = self.client.messages.create(
                body=body,
                from_=self.from_,
                to=to
            )
            return text.body
        except Exception as e:
            print(e)
