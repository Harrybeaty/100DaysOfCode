import random

# input form user, rock paper scissors
player = int(input("Input 0 for Rock, 1 for Paper and 2 for Scissors: "))
# random generator for computers input
comp = random.randint(0, 2)
print(f"Computer's choice: {comp}")
# if logic
if player >= 3 or player < 0:
    print("You typed an invalid number, try again.")
elif player == 0 and comp == 2:
    print("You Win!")
elif comp == 0 and player == 2:
    print("You Lose")
elif comp > player:
    print("You Lose")
elif player > comp:
    print("You Win!")
elif comp == player:
    print("Draw")
