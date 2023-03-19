#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lst = number % 10
else:
    lst = (-number % 10) * -1

if lst > 5:
    print("Last digit of {:d} is {} and is greater than 5".format(number, lst))
elif lst == 0:
    print("Last digit of {:d} is {} and is 0".format(number, lst))
elif lst < 6 and lst != 0:
    print("Last digit of {: d} is {} ".format(number, lst))
    print("and is less than 6 and not 0")
