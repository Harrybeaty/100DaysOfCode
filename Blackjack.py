import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cards_dict = {}

def calc_totals():
    user_total = sum(cards_dict["user"])
    dealer_total = sum(cards_dict["dealer"])
    if user_total > dealer_total:
        print("You Win")
    elif user_total == dealer_total:
        print("It's a Draw")
    else:
        print("You Lose")

def ace_check(hand):
    for card in hand:
        
        return hand
# While game running
run = True
while run:
    init_round = input("Do you want to play a round of Black Jack? (y/n)")
    if init_round == "n":
        run = False
        exit
    else:
        # Select 2 random cards for use and 1 random card for dealer.
        cards_dict["user"] = random.choices(cards, k=2)        # .sample returns a list.
        cards_dict["dealer"] = random.choices(cards, k=2)
        dealer_total = sum(cards_dict["dealer"])
        user_total = sum(cards_dict["user"])
        print(f"Your cards: {cards_dict['user'][0]}, {cards_dict['user'][1]} Dealers card: {cards_dict['dealer'][0]}")
        twist = True
        while twist:
            another_card = input("Do you want to Stick or Twist? ").lower()
            if another_card == "stick":
                twist = False
                # Draw a card for dealer while total is less than 17
                while dealer_total < 17:
                    dealer_new_card = random.choice(cards)
                    print(f"Drawn dealer card: {dealer_new_card}")
                    cards_dict["dealer"].append(dealer_new_card)
                    dealer_total = sum(cards_dict["dealer"])
                    # need to check if dealer is bust.
                    if dealer_total > 21:
                        for card in cards_dict["dealer"]:
                            if card == 11:
                                ace_index = cards_dict["dealer"].index(card)
                                cards_dict["dealer"][ace_index] = 1
                        dealer_total = sum(cards_dict["dealer"])
                        if dealer_total > 21:
                            print(f"Dealer is bust with a total of {dealer_total}")
                    else:
                        print(f"User total: {user_total}, Dealer total: {dealer_total}")
                        if user_total > dealer_total:
                            print("You Win")
                        elif user_total == dealer_total:
                            print("It's a Draw")
                        else:
                            print("You Lose")
                if dealer_total > 17 and dealer_total < 22:
                    print(f"User total: {user_total}, Dealer total: {dealer_total}")
                    if user_total > dealer_total:
                        print("You Win")
                    elif user_total == dealer_total:
                        print("It's a Draw")
                    else:
                        print("You Lose")
            else:
                # If user twists, draw a card, sum all cards, display all cards
                user_new_card = random.choice(cards)
                print(f"Drawn user card: {user_new_card}")
                cards_dict["user"].append(user_new_card)
                print(f"Your Cards: {cards_dict['user']}")
                user_total = sum(cards_dict["user"])
                # Check if User is Bust
                if user_total > 21:
                    for card in cards_dict["user"]:
                        if card == 11:
                            ace_index = cards_dict["user"].index(card)
                            ace_choice = input("Would you like to change your ace value to 1? y/n:")
                            if ace_choice == "y":
                                cards_dict["user"][ace_index] = 1
                        user_total = sum(cards_dict["user"])
                    if user_total > 21:
                        twist = False
                        print(f"You are bust as total is {user_total}")
                    # Check if user has an Ace and change the value to 1           