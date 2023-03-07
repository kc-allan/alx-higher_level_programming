#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
number1 = str(number)
last_digit = number1[-1]
if number < 0:
    last_digit = f"-{last_digit}"
last = int(last_digit)
temp = f"Last digit of {number} is {last_digit}"
if last > 5:
    print(f"{temp} and is greater than 5")
elif last == 0:
    print(f"{temp} and is 0")
else:
    print(f"{temp} and is less than 6 and not 0")
