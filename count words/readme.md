
# Problem Statement

Greetings!

When solving this week's exercise, make sure to hold off on searching directly for the answer on Google/StackOverflow. 🚫🔍

This is a fairly general exercise and there are a number of answers to it. I'd like you to struggle to come to an answer or two (or five?) on your own.

I want you to write a function that accepts a string and returns a mapping (a dictionary or dictionary-like structure) that has words as the keys and the number of times each word was seen as the values.

Your function should work like this:

```
>>> count_words("oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
>>> count_words("don't stop believing")
{"don't": 1, 'stop': 1, 'believing': 1}
```

## Bonus 1

As a bonus, make sure your function works well with mixed case words:
```
>>> count_words("Oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
```
## Bonus 2

For even more of a bonus try to get your function to ignore punctuation outside of words:
```
>>> count_words("Oh what a day, what a lovely day!")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
```
## Hints

Hints for when you get stuck (hover over links to see what they're about):

- Getting a list of words from a sentence
- Checking existence of a given word (key) in dictionary
- Initializing a key to a unique default value in a dictionary
- Various techniques for counting words in a sentence
- [Ignoring punctuation marks while extracting words](https://stackoverflow.com/questions/37543724/python-regex-for-finding-all-words-in-a-string/37543765#37543765)

## Tests

You'll need to write your function in a module named count.py next to the test file. To run the tests you'll run "python test_count.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly. You'll see those noted in the test file.
