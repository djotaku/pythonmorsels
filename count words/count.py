from collections import Counter
import re


def count_words(phrase):
    counter = Counter()
    sentence_list = phrase.lower().split(" ")
    # regular expression to get rid of punctuation.
    front_pattern = re.compile('\A\W\w')
    end_pattern = re.compile('\w+\W$')
    for word in sentence_list:
        if front_pattern.match(word):
            word = word[1:]
        elif end_pattern.match(word):
            word = word[:-1]
        counter[word] += 1
    return counter
