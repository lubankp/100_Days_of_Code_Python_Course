from twilio.rest import Client
import requests

account_sid = "AC3a99640e24bc06a3a7c0f2d556aabb74"
auth_token = "63158653b4d5100b098f4fb8cc2c97d5"


API_KEY = "2e4b0e229a329dd1965291a99fcb861b"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    "lat": 52.229675,
    "lon": 21.012230,
    "appid": API_KEY,
}
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

if weather_data["weather"][0]["id"] < 900:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring umbrella ☂️.",
        from_='+12706757625',
        to='+48697020791'
    )
    print(message.status)
