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
        print(f"Your cards: {cards_dict['user'][0]}, {cards_dict['user'][1]} Dealers card: {cards_dict['dealer'][0]}")
        twist = True
        while twist:
            another_card = input("Do you want to Stick or Twist? ").lower()
            if another_card == "stick":
                twist = False
                # Draw a card for dealer while total is less than 17
                while sum(cards_dict["dealer"]) < 17:
                    dealer_new_card = random.choice(cards)
                    print(f"Drawn card: {dealer_new_card}")
                    cards_dict["dealer"].append(user_new_card)
                    # need to check if dealer is bust.
                    dealer_total = sum(cards_dict["dealer"])
                    if dealer_total > 21:
                        print("Dealer is bust, you win.")
                    # if dealer bust check they if they have an ace.
                calc_totals()
            else:
                # If user twists, draw a card, sum all cards, display all cards
                user_new_card = random.choice(cards)
                print(f"Drawn card: {user_new_card}")
                cards_dict["user"].append(user_new_card)
                user_total = sum(cards_dict["user"])
                print(f"Your Cards: {cards_dict["user"]}")
                # Check if User is Bust
                if user_total > 21:
                    twist = False
                    print("You are Bust!")
                    # Check if user has an Ace and change the value to 1           