def parse_ranges(string):
    ranges = string.split(',')
    iterable = []
    for item in ranges:
        number = item.split('-')
        for thing in number:
            try:
                int(thing)
            except ValueError:
                number.remove(thing)
        for numeral in range(int(number[0]), int(number[-1])+1):
            iterable.append(numeral)
    print(iterable)
    return iterable


if __name__ == "__main__":
    parse_ranges('1-2,4-4,8-10')