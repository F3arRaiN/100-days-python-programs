from art import logo

def add(n1, n2):
    """Adds two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts to numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies to numbers"""
    return n1 * n2

def divide(n1, n2):
    """Divides to numbers"""
    return n1 / n2


operations = {
    # """ These functions have been called but not triggered.
    #         Functions are triggered using the braces/ parenthesis/ ()
    # """
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculation(n1, n2, selected_operator):
    """This function checks the users operator and performs the corresponding operation"""
    return operations[selected_operator](n1, n2)

def first_input():
    """This function returns the user's first number"""
    n1 = float(input("What's the first number?: "))
    return n1

def next_input():
    """This function returns the user's next number"""
    n2 = float(input("What's the next number?: "))
    return n2

def operation_selector():
    """This function displays and returns an operator selected by the user"""
    for key in operations:
        print(key)
    operator = input("Pick an operation: ")
    return operator

print(logo)
first_number = first_input()
operator = operation_selector()
next_number = next_input()
answer = calculation(first_number, next_number, operator)
print(f"{round(first_number, 1)} {operator} {next_number} = {answer}")

running = True
while running:
    keep_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:" ).lower()

    if keep_calculating == "y":
        prev_answer = answer
        for key in operations:
            print(key)
        operator = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        answer = calculation(answer, next_number, operator)
        print(f"{round(prev_answer, 1)} {operator} {next_number} = {answer}")

    elif keep_calculating == "exit":
        running = False

    else:
        print("\n" * 20)
        print(logo)
        first_number = first_input()
        operator = operation_selector()
        next_number = next_input()
        answer = calculation(first_number, next_number, operator)
        print(f"{round(first_number, 1)} {operator} {next_number} = {answer}")
