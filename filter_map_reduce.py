# Examples of using lambda functions with
# filter, map, and, reduce

# eine einfache Lambda-Funktion allein
square = lambda x: x*x
print(square(5))

# filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
# passing in an already defined lambda
squared_numbers = list(map(square, numbers))
print(squared_numbers)
# cubing numbers
cubed_numbers = list(map(lambda x: x ** 3, numbers))
print(cubed_numbers)

# reduce
# reduce(function, iterable, optional_initial_value)
# the function must have exactly two parameters
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
# with an optional argument
product = reduce(lambda x, y: x * y, numbers, 10)
print(product)