bid_dict = {}

print("Welcome to the secret auction")
user_present = "yes"

def max_bid(user_bids):                 # Could use max function thats built into python to be concise.
    max = bid
    max_name = user_name
    for bidder in user_bids:
        if bid_dict[bidder] > max:
            max = user_bids[bidder]
            max_name = bidder
    print(f"{max_name} is the highest bidder!!!")

while user_present == "yes":
    print("\n" * 100)
    user_name = input("What is you name? ")
    bid = int(input("What is your bid? "))
    bid_dict[user_name] = bid
    user_present = input("Is there anyone else to bid? yes/no ")
    if user_present == "no":
        max_bid(bid_dict)
        