from cs50 import *


myName = get_string('Name: ')
myAge = get_int('Age: ')

AgeInTen = myAge + 10

print(f'{myName} will be {AgeInTen} in 10 year\'s time')