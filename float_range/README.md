This week I'd like you to write a callable object called float_range that acts sort of like the built-in range callable but allows for floating point numbers to be specified.

I say "callable" instead of "function" or "class" because I don't actually care how you implement this thing. What I care about is that you can call it and loop over the resulting items.

It should work like this:
```python
>>> for n in float_range(0.5, 2.5, 0.5):
...     print(n)
...
0.5
1.0
1.5
2.0
>>> list(float_range(3.5, 0, -1))
[3.5, 2.5, 1.5, 0.5]
```
Your float_range callable should also allow the step and start arguments to be optional, the same way they are for Python's built-in range callable:
```python
>>> for n in float_range(0.0, 3.0):
...     print(n)
...
0.0
1.0
2.0
>>> for n in float_range(3.0):
...     print(n)
...
0.0
1.0
2.0
```
I also want you to make sure that calling float_range doesn't create a large list of numbers. By this I mean that calling float_range should be memory-efficient. Return an iterator or a generator or some kind of lazy object, not a list.

There are three bonuses this week. Please make sure to attempt the base problem first before attempting any of the bonuses this week. Note that you'll be able to get away with using a function in the base problem, though you'll need a class by the time you get to bonus 1.

## Bonus 1

For the first bonus, I'd like you to make sure the object you get back when calling float_range has a length ✔️:
```python
>>> len(float_range(0.5, 2.5, 0.5))
4

Your float_range objects should also be able to be looped over multiple times at this point:

>>> r = float_range(0.5, 2.5, 0.5)
>>> list(r)
[0.5, 1.0, 1.5, 2.0]
>>> list(r)
[0.5, 1.0, 1.5, 2.0]
```
Note that when it comes to the step values, the length should work similar to the way range objects work:
```python
>>> len(float_range(5, 10, 1.5))
4
>>> len(float_range(10, 5, 1.5))
0
>>> len(float_range(10, 5, -1.5))
4
>>> len(float_range(5, 10, -1.5))
0
```
A hint for the first bonus: if you were using a generator function before, you're probably going to need to switch to creating a float_range class now instead.

## Bonus 2

For the second bonus, I'd like you to make sure the object is reversible with the built-in reversed function ✔️:
```python
>>> list(reversed(float_range(0.5, 2.5, 0.5)))
[2.0, 1.5, 1.0, 0.5]
```
## Bonus 3

The third bonus is a tricky one.

For the third bonus, I'd like you to make sure that you can take the object returned from float_range and ask if it's equal to another object returned from float_range ✔️:
```python
>>> a = float_range(0.5, 2.5, 0.5)
>>> b = float_range(0.5, 2.5, 0.5)
>>> c = float_range(0.5, 3.0, 0.5)
>>> a == b
True
>>> a == c
False
```
In fact I'd like you to take that a step further and make sure that float_range can be compared to range objects and that it allows other objects to be compared to itself without raising an exception:
```python
>>> float_range(5) == range(0, 5)
True
>>> float_range(4) == range(5)
False
>>> float_range(4) == 3
False
```

## Hints

Here are some hints you can use when you get stuck:

- [What are callables?](https://treyhunner.com/2019/04/is-it-a-class-or-a-function-its-a-callable/)
- [An example solution](https://stackoverflow.com/a/51676957/2633215)
- [Optional function arguments](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- Returning an iterator
- Classes and object-oriented programming
- Understanding iterators in detail
- [Returning length of custom object](https://stackoverflow.com/questions/15114023/using-len-and-def-len-self-to-build-a-class)
- A reversible iterable
- Implementing equality checks

## Tests

You'll need to write your code in a module named float_range.py next to the test file. To run the tests you'll run "python test_float_range.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.