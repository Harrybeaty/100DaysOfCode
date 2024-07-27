import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
blank = []
for i in range(word_length):
    blank.append("_")

end_of_game = False
lives = 6
from hangman_art import logo, stages
print(logo)
guessed_letters = []  

while not end_of_game:
    user_letter = input("Please choose a letter: ").lower()  

# Update blank if letter in word.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_letter:
            blank[position] = letter

# Lose a life when letter not in word.
    if user_letter not in blank:
        print(f"You guessed '{user_letter}' which is not in the word, you lose a life.")
        lives -= 1

    guessed_letters.append(user_letter)   
    print(stages[lives])
    print(f"Previously guessed letters: {guessed_letters}")                                            # Print Ascii Art.
# Lose when user has no lives.
    if lives == 0:
        end_of_game = True
        print("You Lose!")
        print(f"The word was {chosen_word}")

    print(blank)

# Win game when blank contains the word.
    if "_" not in blank:
        end_of_game = True
        print("You Win!")

