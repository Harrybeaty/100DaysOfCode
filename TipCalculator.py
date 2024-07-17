print("Welcome to the tip calculator!\n")
bill = int(input("What is the total of the bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
tip_as_percent = tip/100
pay = (bill + (bill * tip))/num_people
final_amount = round(pay, 2)
print(f"Each person should pay: ${final_amount}") 