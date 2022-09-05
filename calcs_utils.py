def take_input():
    num_1 = input("Please enter first number")
    # print(type(num_1))
    num_2 = input("Please enter second number")
    # print(type(num_2))
    print(f"your numbers are {num_1},{num_2}")
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except:
        print("Non numbers received, Please enter numbers")
        return -1, num_1, num_2

    return 0, num_1, num_2


def add_numbers(num_1, num_2):
    ans = num_1 + num_2
    return ans


def subtract_numbers(num_1, num_2):
    ans = num_1 - num_2
    return ans


def multiplication_numbers(num_1, num_2):
    ans = num_1 * num_2
    return ans


def division_numbers(num_1, num_2):
    ans = num_1 / num_2
    return ans


def ask_operation():
    op = input("""Which operation do you want to perform?
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    Please enter one of the number 1/2/3/4

    """)

    try:
        op = int(op)
    except:
        print("no. received is not integer please enter the integer")
        return -1, op

    if op > 0 and op < 5:
        return 0, op
    else:
        return -1, op

