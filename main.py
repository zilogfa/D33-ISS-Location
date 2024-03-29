# API Application Programming Interfaces - send email if ISS location is above you,and it's night - Dev Ali JB 2022

import requests
import datetime as dt
import smtplib
import time


MY_LAT = 47.610149
MY_LONG = -122.201515
MY_EMAIL = "zilogfa@gmail.com"
MY_PASSWORD = "sakseyklbmhbczcl"


def is_iss_overhead():
    """Return True if ISS Location is near Bellevue,WA +=5"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_position = (iss_longitude, iss_latitude)

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
        # Means: ISS location is close by +-5


def is_night():
    """return True if It's Dark | TimeNow vs SUNSET/SUNRISE Bellevue,WA"""

    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
        # Means it's Dark




while True:
    time.sleep(60)  # will run every 60 secs
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up, ISS is here\n\nThe ISS is above you in the sky.")


# window.mainloop()
