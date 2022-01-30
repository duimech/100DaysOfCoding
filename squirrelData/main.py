# This program pulls information from a CSV file, collects specific data, and creates a new CSV with the data.
# Author: Ray Bolin
# Date: 1/28/2022
# 100DaysOfCoding

import pandas

data = pandas.read_csv("100DaysOfCoding/squirrelData/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get the column that we are interested in from the CSV.
squirrel_fur_list = data["Primary Fur Color"].to_list()

cinnamon = squirrel_fur_list.count("Cinnamon")
gray = squirrel_fur_list.count("Gray")
black = squirrel_fur_list.count("Black")

# Put the data into a dictionary to be converted to a DataFrame.
squirrel_dictionary = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Amount": [cinnamon, gray, black]
}

# Convert the data and write the new file.
dataframe = pandas.DataFrame.from_dict(squirrel_dictionary)
dataframe.to_csv("100DaysOfCoding/squirrelData/squirrel_count.csv")