#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 101):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print("{:d}".format(i), " " if i < 101 else end="\n")
