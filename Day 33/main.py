import requests
from datetime import datetime
import time
from smtplib import *

my_email = "pawel.lubanski.91@gmail.com"
password = "wdaiocsapajywwnn"

MY_LAT = 52.229675
MY_LOG = 21.012230


def if_iss_over():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LOG - 5 <= longitude < MY_LOG + 5:
        return True
    else:
        return False


is_over = if_iss_over()


def is_night():
    parameters = {
        "lat": MY_LAT,
        "log": MY_LOG,
        "formatted": 0,
    }

    response1 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response1.raise_for_status()
    data1 = response1.json()
    sunrise = int(data1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data1["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if sunrise < time_now.hour < sunset:
        return False
    else:
        return True

while True:
    time.sleep(60)
    if if_iss_over() and is_night():
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="lubpaw91@gmail.com",
                msg="Subject:ISS\n\n Look Up "
            )
