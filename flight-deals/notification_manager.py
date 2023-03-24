from dotenv import load_dotenv
import os
from twilio.rest import Client

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv('TWILIO_AUTH')

client = Client(account_sid, auth_token)
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, message):
        message = self.client.messages.create(
            body=message,
            from_='+18665167229',
            to='+14154256678'
        )

        print(message.sid)