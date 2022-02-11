# This program checks todays date and checks for matching birthdays in a csv file, then chooses a random birthday letter to send to the receipient.
# Author: Ray Bolin
# Date: 2/9/2022
# 100DaysOfCoding

import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
df = pandas.read_csv("100DaysOfCoding/birthdayWisher/birthdays.csv")
new_dict = df.to_dict("records")
birthday_name_list = []

for row in new_dict:
    if row["month"] == now.month:
        if row["day"] == now.day:
            # Append the entire row which will be a dictionary
            birthday_name_list.append(row)


if len(birthday_name_list) > 0:
    for dictionary in birthday_name_list:
        with open(f"100DaysOfCoding/birthdayWisher/letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            temp_letter = letter.read()
            temp_letter = temp_letter.replace("[NAME]", dictionary["name"])

        with smtplib.SMTP("smtp.domain.tld", 587) as mailer:
            username = "username"
            password = "password"
            from_addr = "from_addr@domain.tld"
            to_addr = dictionary["email"]
            mailer.ehlo()
            mailer.starttls()
            mailer.login(username, password)
            mailer.sendmail(from_addr,to_addr,msg=f"From: {from_addr}\n\nTo: {from_addr}\n\n, Subject: Happy Birthday!\n\n{temp_letter}\n")

