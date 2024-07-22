import random

# get inputs
length = int(input("How long does your password need to be? "))
num_symbols = int(input("How many symbols? "))
num_numbers = int(input("How many numbers? "))
num_letters = length - num_numbers - num_symbols

# database of chars
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# create empty string
password_list = []

#letters
for char in range(1, num_letters+1):
    password_list.append(random.choice(letters))

# symbols
for char in range(1, num_symbols+1):
    password_list.append(random.choice(symbols))

# numbers

for char in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))

# shuffle
random.shuffle(password_list)
password = ''.join(password_list)
print(password)