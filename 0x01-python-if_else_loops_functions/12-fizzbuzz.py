#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Print the nums from 1 to 100 separated by space.

    For multiples of three, prnt Fizz instead of the num.
    For multiples of five, prnt Buzz instead of the num.
    For multiples of three and five, prnt FizzBuzz instead of the num.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")

