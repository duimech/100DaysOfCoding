# This program is a calculator that uses functions that are kept in a dictionary
# Author: Ray Bolin
# Date: 1/9/2022
# 100DaysOfCoding


# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Print operations (keys from the dictionary) for the user to select
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def print_operations():
  for key in operations:
    print(key)


should_continue = "y"
answer = ""

while should_continue == "y":
    if answer != "":
        num1 = answer 
    else:
        num1 = float(input("What is the first number:  "))

    print_operations()
    operation_symbol = input("Select an operation:  ")
    num2 = float(input("What is the next number:  "))
    answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    should_continue = input(f"Type y to continue calculating with the number {answer} type n to exit or c to clear operations and continue:  ")
    if should_continue == "c":
        answer = ""
        should_continue = "y"

