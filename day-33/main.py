import smtplib
from datetime import datetime
import time
import requests

MY_LAT = 18.097188355897398
MY_LONG = 83.39902006806793

MY_EMAIL = "saikumarseepana436@gmail.com"
MY_PASSWORD = "123456"

def is_iss_overhead():
    response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
    response.raise_for_status()
    data = response.json()

    iss_longitude = int(data["longitude"])
    iss_latitude = int(data["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up ☝\n\n The ISS is above you"
        )