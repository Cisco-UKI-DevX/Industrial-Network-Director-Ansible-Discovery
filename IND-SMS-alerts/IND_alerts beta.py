
import twilio
import requests
import json

from twilio.rest import Client

IP = raw_input("Please enter your Industrial network director IP address: ")
username = raw_input("Please enter your Industrial network director username: ")
password = raw_input("Please enter your Industrial network director password: ")
SENDING_MOB_NO = raw_input ("Please enter your twilio mobile number: ")
MOB_NO = raw_input ("Please enter your mobile number: ")
account_sid = raw_input ("and finally, this application uses Twilio. Please enter your Twilio account SID: ")
auth_token = raw_input ("and finally, this application uses Twilio. Please enter your Twilio auth key: ")

# Your Account Sid and Auth Token from twilio.com/console

# api-endpoint
URL = "https://" + IP + ":8443/api/v1/alarms?limit=1"

r = requests.get(URL, verify=False, auth=(username, password))

response = json.loads(r.text)

previd = response['records'][0]['id']

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Alerting initialised, when new alerts are created you will be messaged",
                     from_=SENDING_MOB_NO,
                     to=MOB_NO
                 )

print(message.sid)


while True:

    r = requests.get(URL, verify=False, auth=(username, password))

    response = json.loads(r.text)

    id = response['records'][0]['id']

    if (id > previd){

    message = client.messages \
                    .create(
                         body="ALERT" + response['records'][0]['message'],
                         from_=SENDING_MOB_NO,
                         to=MOB_NO
                     )

    print(message.sid)

    previd = id
    }

    time.sleep(60)
