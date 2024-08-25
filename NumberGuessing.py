# Computer selects a random number.
import random

easy_lives = 10
hard_lives = 5

def check_answer(guessed_number, comp_number, lives):
    if guessed_number > comp_number:
        print("Too High!!")
        return lives - 1
    elif guessed_number < comp_number:
        print("Too Low!!")
        return lives - 1
    else:
        print("Correct, You Win")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    # Select number of lives.
    if difficulty == 'easy':
        return easy_lives
    elif difficulty == 'hard':
        return hard_lives
    
comp_number = random.randint(1,100)
print(comp_number)
# Choose whether the game is easy or hard.
lives = set_difficulty()
print(f"You have {lives} lives.")
guessed_number = 0
# while guessed number isn't computer number or lives is above 0.
while guessed_number != comp_number and lives != 0:
    # User guesses a number.
    guessed_number = int(input("Make a guess: "))
    # Check if number is the right number.
    lives = check_answer(guessed_number, comp_number, lives)
    if lives != None:
        print(f"Lives Remaining: {lives}")
# If user runs out of lives display you lose and display the computers number.
if lives == 0:
    print(f"You Lose, The number was {comp_number}")
