#!/usr/bin/python3
for i in range(25, -1, -1):
    d = i + ord('A')
    if i % 2 == 1:
        d += 32
    print("{:c}".format(d), end="")
