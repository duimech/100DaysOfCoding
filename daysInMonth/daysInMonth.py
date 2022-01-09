# This program returns the days in month and is accurate for leap year too.
# Author: Ray Bolin
# Date: 1/9/2022
# 100DaysOfCoding

def is_leap(year):
  """Determine if the year is leap year"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  
  if is_leap(year) and month == 2:
      days = 29
      return days

  days = month_days[month - 1]
  return days 


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"There are {days} in the month chosen")







