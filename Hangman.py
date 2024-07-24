import random

word_list = ["ardvark", "carrot", "tiger", "chicken", "dog"]

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
blank = []
for i in range(word_length):
    blank.append("_")

user_letter = input("Please choose a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == user_letter:
        print("right")
        blank[position] = letter
    else:
        print("wrong")

print(blank)