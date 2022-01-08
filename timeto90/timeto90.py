# This programs calculates how many days, weeks, and months you have until age 90
# Author: Ray Bolin
# Date: 1/1/2022
# 100DaysOfCoding

age = input("What is your current age?")

nintyDaysTotal = 90 * 365
nintyWeeksTotal = 90 * 52
nintyMonthsTotal = 90 * 12

age = int(age)
ageDays = age * 365
ageWeeks = age * 52
ageMonths = age * 12

diffDays = nintyDaysTotal - ageDays
diffWeeks = nintyWeeksTotal - ageWeeks
diffMonths = nintyMonthsTotal - ageMonths

print(f"You have {diffDays} days, {diffWeeks} weeks, and {diffMonths} months left.")
