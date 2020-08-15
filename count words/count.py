from collections import Counter
import re


def count_words(phrase):
    return Counter(re.findall(r"\b[\w'-]+\b", phrase.lower()))

# the findall creates a list for counter to iterate over and count items
