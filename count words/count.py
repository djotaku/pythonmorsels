from collections import Counter


def count_words(phrase):
    counter = Counter()
    sentence_list = phrase.lower().split(" ")
    for word in sentence_list:
        counter[word] += 1
    return counter

