# This program determines if a number is prime or not
# Author: Ray Bolin
# Date: 1/6/2022
# 100DaysOfCoding

def prime_checker(number):
  maxtest = number
  zero_count = 0

# Starting range at 2 since prime numbers are divisible by 1 and itself. 
# Using range and the number since range will go to 1 less than the number

  for num in range(2,maxtest):
    if number % num == 0:
      zero_count += 1

  if zero_count == 0:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)



