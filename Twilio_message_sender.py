from twilio.rest import Client

account_sid = "Enter your acc sid"
auth_token = "Enter Your auth token"

twilio_number = "Enter your number received via TWILIO"
my_phone_number = "Enter number to which alert will be sended"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Enter Message", from_=twilio_number, to=my_phone_number
)
# print(message.body)
