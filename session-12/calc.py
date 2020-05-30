def add_values(x, y):
    return x + y


def multiply_values(x, y):
    return x * y


def divide_values(x, y):
    return x // y


if __name__ == "__main__":
    print(add_values(20, 30) == 50)
    print(multiply_values(20, 30) == 600)
    print(divide_values(120, 30) == 4)
