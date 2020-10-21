import math


def is_perfect_square(number):
    return math.sqrt(number) == int(math.sqrt(number))


if __name__ == "__main__":
    print(is_perfect_square(9))
