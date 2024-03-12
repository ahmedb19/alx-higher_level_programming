#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number > 0):
    print('{:d} is positive', number)
else...if (number == 0):
    print('{:d} is zero', number)
else:
    print('{:d} is negative', number)
