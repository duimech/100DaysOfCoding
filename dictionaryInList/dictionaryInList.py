# This program uses a function to add a dictionary to an existing list of dictionaries
# Author: Ray Bolin
# Date: 1/8/2022
# 100DaysOfCoding

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, townlist):
    # country = country
    # visits = visits
    # townlist = townlist

    new_country = {
        "country": country,
        "visits": visits,
        "cities": townlist,
    }

    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
