#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    rem = number % 10
    if rem > 5:
        print(f"Last digit of {number} is {rem} and is greater than 5")
    elif rem == 0:
        print(f"Last digit of {number} is {rem} and is 0")
    elif rem > 0 and rem < 5:
        print(f"Last digit of {number} is {rem} and is less than 6 and not 0")
else:
    rem = int(repr(number)[-1])
    rem = rem * -1
    print(f"Last digit of {number} is {rem} and is less than 6 and not 0")
