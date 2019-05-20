
# This application uses Twilio to send sms messages. Create an account at https://www.twilio.com.
# To install Twilio python module, run 'pip install twilio'
import requests
import json
import time
import getpass
from twilio.rest import Client

# Get setup info
IP = input("\nPlease enter your Cisco Industrial Network Director IP address: ")
username = input("Please enter your Cisco Industrial Network Director username: ")
password = getpass.getpass(prompt="Please enter your Cisco Industrial Network Director password: ")
MOB_NO = input ("Please enter the mobile number sms alerts are sent to (include country code): ")
print("\nThis application uses Twilio to send sms alerts. You can create an account at https://www.twilio.com")
SENDING_MOB_NO = input ("Please enter your Twilio mobile number (include country code): ")
account_sid = input ("Please enter your Twilio account SID: ")
auth_token = input("Please enter your Twilio auth key: ")

# Industrial Network Director API
URL = "https://" + IP + ":8443/api/v1/alarms?limit=1"
r = requests.get(URL, verify=False, auth=(username, password))
response = json.loads(r.text)
previd = response['records'][0]['id']
client = Client(account_sid, auth_token)
# Send inital startup sms message
message = client.messages \
                .create(
                     body="Alerting initialised, when new alerts are created you will be messaged",
                     from_=SENDING_MOB_NO,
                     to=MOB_NO
                 )
print(message.sid)

# Output startup message to terminal
print("\n***** System Started - Now listening for new alerts *****\n")

# Monitor for new alerts
while True:
    r = requests.get(URL, verify=False, auth=(username, password))
    response = json.loads(r.text)
    id = response['records'][0]['id']
    if id > previd:
        message = client.messages \
                        .create(
                             body="ALERT" + response['records'][0]['message'],
                             from_=SENDING_MOB_NO,
                             to=MOB_NO
                         )
        print(message.sid)
        previd = id
    time.sleep(60)
