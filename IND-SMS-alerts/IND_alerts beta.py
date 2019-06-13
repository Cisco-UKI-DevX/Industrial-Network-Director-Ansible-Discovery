
# This application uses Twilio to send sms messages. Create an account at https://www.twilio.com.
# To install Twilio python module, run 'pip install twilio'


#Copyright (c) 2019 Cisco and/or its affiliates.

#This software is licensed to you under the terms of the Cisco Sample
#Code License, Version 1.1 (the "License"). You may obtain a copy of the
#License at

#               https://developer.cisco.com/docs/licenses

#All use of the material herein must be in accordance with the terms of
#the License. All rights not expressly granted by the License are
#reserved. Unless required by applicable law or agreed to separately in
#writing, software distributed under the License is distributed on an "AS
#IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#or implied.

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
