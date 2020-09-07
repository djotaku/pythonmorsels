I want you to write a function that accepts two strings and returns True if the two strings are anagrams of each other.

Your function should work like this:
```python
>>> is_anagram("tea", "eat")
True
>>> is_anagram("tea", "treat")
False
>>> is_anagram("sinks", "skin")
False
>>> is_anagram("Listen", "silent")
True
```
Make sure your function works with mixed case.

Before you try to solve any bonuses, I recommend you try to find at least two ways to solve this problem.

Okay now to the bonuses...

Bonus 1

For the first bonus, make sure your function ignores spaces ✔️:
```python
>>> is_anagram("coins kept", "in pockets")
True
```
Bonus 2

For a second bonus, make sure your function also ignores punctuation ✔️:
```python
>>> is_anagram("a diet", "I'd eat")
True
```
Bonus 3

If you solved this one really quickly, here's a more challenging third bonus for you: try allowing accented latin1 characters but ignoring the accent marks. ✔️
```python
>>> is_anagram("cardiografía", "radiográfica")
True
```
Hints

Hints for when you get stuck (hover over links to see what they're about):

- Counting the number of times each letter occurs
- Setting the default value of a key in a dictionary
- A variety of different ways to count the number of times each word is seen
- A different way to solve the base problem
- Comparing strings case-insensitively
- Ignoring spaces during comparisons
- Removing punctuation characters from strings
- [Removing accents from characters](https://stackoverflow.com/questions/14682397/how-does-unicodedata-normalizeform-unistr-work/14682498#14682498)

# Tests

You'll need to write your function in a module named anagram.py next to the test file. To run the tests you'll run "python test_anagram.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly. You'll see those noted in the test file.