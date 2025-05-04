# This is the class that send SMS messages with the flight deals

import os
import requests
from dotenv import load_dotenv
from twilio.jwt.access_token import AccessToken
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_TO_PHONE_NUMBER")

# Debugging: Print loaded environment variables (remove in production)
if not all([TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_VIRTUAL_NUMBER, TWILIO_VERIFIED_NUMBER]):
    raise ValueError("One or more Twilio environment variables are missing. Please check your .env file.")


# NotificationManager class
class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, data):
        """
        Sends a message containing flight deals using the Twilio API.

        Args:
            message (str): The content of the message to be sent.

        Returns:
            None

        Raises:
            Exception: If the message fails to send, an exception is caught and an error message is printed.
        """
        # This method is for sending messages with the flight deals
        try:
            message = self.client.messages.create(
                body=data,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER
            )
            print(f"Message sent: {message.sid}")
        except Exception as e:
            print(f"Failed to send message: {e}")
