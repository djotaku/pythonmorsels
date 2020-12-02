# Problem Statement

Hiya!

This week I'd like you to write a function that takes a nested list of numbers and adds up all the numbers.

The phrase "nested list of numbers" might not be obvious. Here are examples of what I mean:
```python
>>> deep_add([1, 2, 3, 4])
10
>>> deep_add([[1, 2, 3], [4, 5, 6]])
21
>>> deep_add([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
36
```
So your deep_add function should accept lists of numbers, lists of lists of numbers, lists of lists of lists of numbers, and so on. It should even work when there are multiple hierarchies involved or when there are empty lists:
```python
>>> deep_add([1, [2, [3, 4], [], [[5, 6], [7, 8]]]])
36
>>> deep_add([[], []])
0
```
## Bonus 1

For the first bonus this week, I'd like you to make sure your function works with any iterable, not just lists. It should work with tuples, sets, and even generators ✔️:
```python
>>> deep_add([(1, 2), [3, {4, 5}]])
15
```
## Bonus 2

For the second bonus I'd like you to allow your function to accept an optional start value (which defaults to 0) ✔️:
```python
>>> deep_add([[1, 2], [3, 4]], start=2)
12
```
## Bonus 3

For the third bonus, make sure your function works with anything number-like (anything you can use + on except for iterables), not just numbers themselves ✔️:
```python
>>> from datetime import timedelta
>>> deep_add([[timedelta(5), timedelta(10)], [timedelta(3)]], start=timedelta(0))
18
```
While you're at it, see if you can find a few different ways to solve this exercise. If you need a hint, read the fine print at the end of this email.

Hints

Hints for when you get stuck (hover over links to see what they're about):

- Verifying if a given argument is a list
- A talk on recursion
- Summing list elements recursively
- A built-in function for adding numbers
- Bonus 1: a hint for type-checking numbers
- Bonus 2: What to do with your start value
- Bonus 3: checking for "iterables" instead of numbers

Tests

You'll need to write your function in a module named deep_add.py next to the test file. To run the tests you'll run "python test_deep_add.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.