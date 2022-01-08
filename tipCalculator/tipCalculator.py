# This program is a tip calculator
# Author: Ray Bolin
# Date: 1/1/2022
# 100DaysOfCoding

print("Welcome to the tip calculator\n")

totalBill = float(input("What was the total bill? \n"))
numPeople = int( input ("How many people to split the bill? \n"))
tipPercent = int(input("What percentage tip would you like to give? 10, 12, or 15 \n"))

indBill = totalBill / numPeople
indTip = indBill * tipPercent / 100
indBillAndTip = "{:.2f}".format(indBill + indTip)

print(f"Each person should pay ${indBillAndTip}" )
