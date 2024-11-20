#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()

for table in range(11):
    print(f"Table de {table}: ", end="")
    for multiplier in range(11):
        print(table * multiplier, end=" ")
    print()
