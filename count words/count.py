from collections import Counter


def count_words(phrase):
    counter = Counter()
    for word in phrase:
        counter[word] += 1
    return counter
