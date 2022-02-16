# This program gets the ISS position. If its near my location and nighttime then send me an email.
# Author: Ray Bolin
# Date: 2/8/2022
# 100DaysOfCoding

import requests
from datetime import datetime
import smtplib
import time

MY_LONG = -83.916718
MY_LAT = 35.962639

def iss_current_position():
    # Get location of the international space station
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_longitude = data["iss_position"]["longitude"]
    iss_latitude = data["iss_position"]["latitude"]
    return (iss_longitude, iss_latitude)


def iss_near_me(iss_position):
    # See if ISS is near me by plus or minus 5 degrees
    if iss_position[0] in range((int(MY_LONG - 5)),(int(MY_LONG + 5))) and iss_position[1] in range((int(MY_LAT - 5)),(int(MY_LAT + 5))):
        return True
    else:
        return False


def sunrise_sunset_time():
    # Get the sunrise and sunset times at my location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    request = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    request.raise_for_status()
    data_json = request.json()
    # sunrise = data_json["results"]["sunrise"]
    # sunrise = sunrise.split("T")
    # sunrise = sunrise[1].split(":")
    # sunrise = sunrise[0]
    sunrise = data_json["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data_json["results"]["sunset"].split("T")[1].split(":")[0]
    return (sunrise, sunset)


def check_night_time(sunrise_sunset):
    # Check to see if its dark outside at my location
    time_now = datetime.now()

    if time_now.hour in range(0,int(sunrise_sunset[0]) + 1) or time_now.hour in range(int(sunrise_sunset[1]), 24):
        return True
    else:
        return False


def send_mail():
    # Send an email stating to look up to see the ISS
    username = "email@domain.tld"
    password = "email_password"
    from_addr = "email@domain.tld"
    to_addr = "email@domain.tld"

    mailer = smtplib.SMTP("smtp.domain.tld", 587)
    mailer.ehlo()
    mailer.starttls()
    mailer.login(username, password)
    mailer.sendmail(from_addr, to_addr, msg=f"To: {to_addr}\n\nFrom: {from_addr}\n\nSubject: ISS Near\n\nLook up in the sky!")


while True:
    time.sleep(10)
    # Get the ISS position and if its near me and night time then send me an email
    iss_position = iss_current_position()
    if iss_near_me(iss_position):
        sunrise_sunset = sunrise_sunset_time()
        if check_night_time(sunrise_sunset):
            send_mail()
