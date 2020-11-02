I want you to write a function that accepts an iterable and returns a new iterable with all items from the original iterable except for duplicates.

Here's an example:
```python
>>> uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
[1, 2, 3]
>>> nums = [1, -3, 2, 3, -1]
>>> squares = (n**2 for n in nums)
>>> uniques_only(squares)
[1, 9, 4]
```

Note that the order of the returned elements should be the same.

## Bonus 1

As a bonus, return an iterator (for example a generator) from your uniques_only function instead of a list. This should allow your uniques_only function to accept infinitely long iterables (or other lazy iterables). ✔️

## Bonus 2

Here's another bonus to do after you've made your uniques_only function return a lazy iterable: allow your uniques_only function to work with unhashable objects. ✔️

For example when two lists with equal items are provided, they should be seen as duplicates:
```python
>>> list(uniques_only([['a', 'b'], ['a', 'c'], ['a', 'b']]))
[['a', 'b'], ['a', 'c']]
```
## Bonus 3

For an extra bonus, make sure your function works efficiently with hashable items while still accepting unhashable items. ✔️

This one is a little harder to test. There's an automated test (included below) that attempts to performance-test your function.

## Hints

Hints for when you get stuck (hover over links to see what they're about):

- Removing duplicates from a list
- Some clever duplicate-removing code
- [Making a function that returns an iterator](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/)
- What does hashable mean
- Determining whether an item is hashable
- Another way to determine hashabiltiy

## Tests

You'll need to write your function in a module named uniques.py next to the test file. To run the tests you'll run "python test_uniques.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.