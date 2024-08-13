def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations_dict = {
    "+" : add, 
    "-" : minus,
    "*" : multiply,
    "/" : divide
}

def calculator():
    save_answer = True

    num1 = float(input("Input your first number: "))
    while save_answer:
        for key in operations_dict:
            print(key)
        operation = input("Pick an operation +-*/ : ")
        if operation not in operations_dict:
            print("Invalid operation")
        else:
            num2 = float(input("Input your second number: "))

            answer = operations_dict[operation](num1, num2)

            print(f"{num1} {operation} {num2} = {answer}")

            save_answer = input("Would you like to use your last answer in the next calculation? (y/n): ")
            if save_answer == "n":
                save_answer = False
                print("\n"*20)
                calculator()                    # Use recursion to use the calculator over and over.
            else:
                num1 = answer

calculator()