from twilio.rest import Client
class NotificationsHandler:
    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)
    def send_text_message(self, to, from_, body):
        text = self.client.messages.create(to=to, from_=from_, body=body)
        return text