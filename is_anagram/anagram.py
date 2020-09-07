def is_anagram(string1: str, string2: str) -> bool:
    """Returns true if string1 and string2 are anagrams of each other"""
    string1 = string1.replace(" ", '')
    string2 = string2.replace(" ", '')
    if len(string1) != len(string2):
        return False
    else:
        return set(string1.lower()) == set(string2.lower())


if __name__ == "__main__":
    result = is_anagram("tea", "eat")
    print(result)

