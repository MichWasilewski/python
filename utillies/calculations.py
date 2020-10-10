def multiplication(a, b):
    return a * b


def subtraction(a, b):
    return a - b


def addiction(a, b):
    return a + b


def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")

