import re

from unicodedata import normalize


def is_anagram(string1: str, string2: str) -> bool:
    """Returns true if string1 and string2 are anagrams of each other"""
    # get rid of unicode
    string1 = normalize('NFD', string1)
    string2 = normalize('NFD', string2)

    # get rid of all non-alphanumerics
    string1 = re.sub('[^A-Za-z0-9]+', '', string1)
    string2 = re.sub('[^A-Za-z0-9]+', '', string2)

    if len(string1) != len(string2):
        return False
    else:
        return set(string1.lower()) == set(string2.lower())


if __name__ == "__main__":
    result = is_anagram("teá", "eat")
    print(result)

