# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)
message = client.messages.create(
    body = " Faulted Train Track Found, File name : fault.PNG (Size : 314.4KB). Please Take Immediate Actions",
    from_ = keys.twilio_number,
    to = keys.my_phone_number
)

print(message.body)

    
"""
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+919976280070',
                     to='+918300843618'
                 )

print(message.sid)
"""