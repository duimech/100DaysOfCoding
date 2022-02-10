# This program emails a motivational quote from the quotes.txt file if the weekday is Monday
# Author: Ray Bolin
# Date: 2/8/2022
# 100DaysOfCoding

import random
import datetime as dt
import smtplib

my_email = "email@domain"
my_password = "plaintextpassword"
from_address = "from_email@domain"
to_address = "to_email@domain"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("100DaysOfCoding/mondayMotivation/quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.domain.tld", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_address, to_address, msg=f"From: {from_address}\n\nTo:{to_address}\n\nSubject: Monday Motivation\n\nEnjoy this quote:\n\n{quote}")

