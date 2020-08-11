from collections import Counter


def count_words(phrase):
    counter = Counter()
    sentence_list = phrase.split(" ")
    for word in sentence_list:
        counter[word] += 1
    return counter

# first attempt failed because it's counting letters, not words
