from collections import Iterable


def sums(iterable):
    sum = 0
    for number in iterable:
        if isinstance(number, Iterable):
            if len(number) == 0:
                sum = sum + 0
            else:
                sum = sums(number) + sum
        else:
            sum = number + sum
    return sum


def deep_add(iterable):
    # print(f"The iterable {iterable}")
    return sums(iterable)

