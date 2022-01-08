# This program covers fucntions
# Author: Ray Bolin
# Date: 1/6/2022
# 100DaysOfCoding

# def greet():
#     print("Hello")
#     print("My name is Ray")
#     print("How are you")

# greet()


# def greet_name(name):
#     print(f"Hello, {name} ")
#     print("My name is Ray")
#     print("How are you")

# name = input("Type a name: ")
# greet_name(name)

# This shows position arguments
# def greet_with(name, location):
#     print(f"Hello, {name} ")
#     print(f"What is it like in {location}")

# name = input("Type a name: ")
# location = input("Type a location: ")

# greet_with(name, location)

# This shows keyword arguments
def greet_with(location, name):
    print(f"Hello, {name} ")
    print(f"What is it like in {location}")

name = input("Type a name: ")
location = input("Type a location: ")

greet_with(location=location, name=name)

