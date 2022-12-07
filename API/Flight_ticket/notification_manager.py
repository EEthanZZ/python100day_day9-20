from twilio.rest import Client

TWILIO_SID = "AC185eb2acbcdee217a8e18b6a364a56bf"
TWILIO_AUTH_TOKEN = "afbc249ee15408cbd4cb9d34a32d4e8a"
TWILIO_VIRTUAL_NUMBER = "+16614864166"
TWILIO_VERIFIED_NUMBER = "0404346835"
class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_= TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )

        print(message.sid)