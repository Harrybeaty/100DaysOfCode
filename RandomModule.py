import random

random_integer = random.randint(1, 10)
print(random_integer)


random_float = random.random()  # Random float between 0.00 - 0.9999999...
random_float *= 5               # This changes the range to 0.00 - 4.99999999..
print(random_float)