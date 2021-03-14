import requests
import os
from twilio.rest import Client

api_key = "e00be43b04012138ab3273de21df5e25"
URL = "https://api.openweathermap.org/data/2.5/onecall"
MY_LNG = "YOUR LONGITUDE"
MY_LAT = "YOUR LATITUDE"

account_sid = "AC420bdbc44c023c2741f26340345435e9"
# os.environ['TWILIO_ACCOUNT_SID']
auth_token = "7b951f9cb0d3e4d7ec2c8be793744e35"
# os.environ['TWILIO_AUTH_TOKEN']

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_condition = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_condition:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+14242066922',
        to='YOUR NUMBER'
    )

    print(message.sid)