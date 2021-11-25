from numpy import average, sum
from cs50 import get_int


numbers = []
for i in range(3): numbers.append(get_int(f'Number {i + 1}: '))

print(f'Sum is {sum(numbers)}\nAverage is {round(average(numbers), 2)}')