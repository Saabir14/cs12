from cs50 import *


print('Welcome to the meal price splitter')

people = get_int('How many people need to pay? ')
bill = get_float('How much was the bill? ')

print('Each person should pay ', round((bill/people), 2))