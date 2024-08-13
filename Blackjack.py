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
                while sum(cards_dict["dealer"]) < 17:
                    # needs to display card when it is drawn
                    cards_dict["dealer"].append(random.choice(cards))
                    # need to check id dealer is bust.
                    # if dealer bust check they if they have an ace.
                calc_totals()
            else:
                # Needs to display card when it is drawn
                cards_dict["user"].append(random.choice(cards))
                user_total = sum(cards_dict["user"])
                # Needs to display cards
                if user_total > 21:
                    twist = False
                    print("You are Bust!")
                # Need to check if user has ace and change it to 1
                