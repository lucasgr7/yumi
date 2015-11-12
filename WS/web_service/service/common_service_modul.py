# here we create method for common purpose
import random


def getLucky(number):
    return True if random.randint(0, number * 2) <= number else False

