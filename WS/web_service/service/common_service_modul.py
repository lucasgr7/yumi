# here we create method for common purpose
import random


def compare_with_random(number):
    return True if random.randint(0, number * 2) <= number else False

