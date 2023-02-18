
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
