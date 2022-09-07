#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100)
    print(tip)
    tax = meal_cost * (tax_percent/100)
    print(tax)
    totalCost = meal_cost + tip + tax
    return round(totalCost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    x = solve(meal_cost, tip_percent, tax_percent)

    print(x)
