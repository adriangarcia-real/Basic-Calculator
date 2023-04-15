def sum(x, y):
    return x + y


def difference(x, y):
    return x - y


def product(x, y):
    return x * y


def quotient(x, y):
    return x / y


while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter another number: "))
    except ValueError:
        print("Please enter a valid Number!\n")
        continue

    operation = input("Enter operation (+, -, *, /): ")
    if operation == "+":
        print(sum(num_1, num_2))
    elif operation == "-":
        print(difference(num_1, num_2))
    elif operation == "*":
        print(product(num_1, num_2))
    elif operation == "/":
        print(quotient(num_1, num_2))
    else:
        print("Invalid input! (Note: use +, -, *, or / for operations)\n")
        continue

    choice = input("\nWould you like to use it again (y/n)? ")
    if choice.lower() != "y":
        break