# This program is the FizzBuzz game.
# Author: Ray Bolin
# Date: 1/3/2022
# Description: Numbers that are divisible by 3 print Fizz. Numbers that are divisible by 5 print Buzz. Numbers that are divisible by 3 and 5 print FizzBuzz.
# 100DaysOfCoding

for num in range(1,101):
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
