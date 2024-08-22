def deal_card():
    card = random.choice(cards)
    return card

def calculate_total(hand):
    ''' First find if it is a blackjack for the user as this will end the game immediatly no matter what.
        hen second check for an ace and replace it with 1 if the users total is over 21.'''
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    
    return sum(hand)

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = []
dealer_hand = []
is_game_over = False

# Deal cards
for _ in range(2):
    user_hand.append(deal_card())
    dealer_hand.append(deal_card())

# End game if anyone gets blackjack or user is over 21, we will handle the computer later.
user_total = calculate_total(user_hand)
dealer_total = calculate_total(dealer_hand)

# Display cards
print(f"Your Cards: {user_hand}, Your Total {user_total}")
print(f"Dealer's Card: {dealer_hand[0]}")

if user_total == 0 or user_total > 21 or dealer_total == 0:
    is_game_over = True

# While game has not ended, ask user to twist or stick.
while not is_game_over:
    another_card = input("Type 'y' for another card or 'n' to stick: ")
    if another_card == "y":
        user_hand.append(deal_card())
        print(f"Your Cards: {user_hand}, Your Total {user_total}")
    else:
        is_game_over = True

while dealer_total > 17



