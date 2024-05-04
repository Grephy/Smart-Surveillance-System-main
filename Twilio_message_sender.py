from twilio.rest import Client

account_sid = "AC850715c8fdd8532573bd3087f9e1464e"
auth_token = "c6689a884f0d42bdfdd2b4c1d88eb753"

twilio_number = "+18159753495"
my_phone_number = "+919987182137"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Enter Message", from_=twilio_number, to=my_phone_number
)
# print(message.body)
