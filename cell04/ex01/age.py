#!/usr/bin/env python3

current_age = int(input("Please tell me your age: "))

print(f"You are currently {current_age} years old.")
for years in [10, 20, 30]:
    print(f"In {years} years, you'll be {current_age + years} years old.")
