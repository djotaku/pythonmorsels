from collections import Iterable


def sums(iterable, start):
    sum = start
    for number in iterable:
        if isinstance(number, Iterable):
            if len(number) == 0:
                sum = sum + 0
            else:
                sum = sums(number, sum)
        else:
            sum = number + sum
    return sum


def deep_add(iterable, start=0):
    # print(f"The iterable {iterable}")
    return sums(iterable, start)
