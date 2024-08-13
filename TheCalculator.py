# Ask User for number

# Ask User for operation

# Ask User for second number

# pick correct function

# carry out function

# Ask user for another calc with same number
def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

save_answer = True

num1 = float(input("Input your first number: "))
while save_answer:
    operation = input("Pick an operation +-*/ : ")
    num2 = float(input("Input your second number: "))

    if operation == "+":
        answer = add(num1, num2)
    elif operation == "-":
        answer = minus(num1, num2)
    elif operation == "*":
        answer = multiply(num1, num2)
    elif operation == "/":
        answer = divide(num1, num2)

    print(answer)

    save_answer = input("Would you like to use your last answer in the next calculation? (y/n): ")
    if save_answer == "n":
        save_answer = False
    else:
        num1 = answer
