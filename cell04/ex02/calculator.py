#!/usr/bin/env python3
first_number = float(input("Give me the first number: "))
second_number = float(input("Give me the second number: "))
print("Thank you!"
print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")
if second_number != 0:
    print(f"{first_number} / {second_number} = {first_number / second_number}")
else:
    print("Division by zero is not allowed.")
