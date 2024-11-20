#!/usr/bin/env python3
user_input = input("Give me a number: ")
number = float(user_input)
if number % 1 == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")
