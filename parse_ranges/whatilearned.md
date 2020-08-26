# What I Learned

## Base Problem

[Base Solution](https://github.com/djotaku/pythonmorsels/blob/1cbdf7d17e79f1655c59b8bb5595246c89f32bdb/parse_ranges/parse_ranges.py)

As I mentioned in the commit, I spent a long time trying to figure out how to use list comprehension, but I couldn't figure how how to refer to the first list I had to make. (When I did the '-' split). Pretty neat that it also automatically worked for Bonus 2. I think of all the problems I've done for Python Morsels, this is the first time I've been completely convinced I was doing this the worst possible way. If he DOES mention how to do this with list comprehensions, I'd like to see what I was doing wrong.

## Bonus 1

[Bonus 1 Solution](https://github.com/djotaku/pythonmorsels/blob/b20d5460305c869cb325e29fdc601e9da5026bec/parse_ranges/parse_ranges.py)

I think I had a solution that would work for Bonus 1, but the problem is that his unit test has an assertion from 100-1000000000000 and that was killing the computer. It's important to note that I ended up with Solutions Prime and Bonus 2 at once. Then Bonus 3 before I came back to Bonus 1. Essentially, if I could solve the list comprehension, then I could turn it into a generator and it would work - and should work for all solutions. 

I just had to stare at it a bit longer and realize that all I had to do was create a yield where I would have appended. I'm very excited to have made that discovery and doubly so for having puzzled it out on my own. Still can't wait to see what the official solution is supposed to be because it certainly can't be this convoluted mess.

## Bonus 2

[Bonus 2 Solution](https://github.com/djotaku/pythonmorsels/blob/1cbdf7d17e79f1655c59b8bb5595246c89f32bdb/parse_ranges/parse_ranges.py)

Hurray, this just happened to work when I did the Base Problem solution.

## Bonus 3

[Bonus 3 Solution](https://github.com/djotaku/pythonmorsels/blob/1b427234192795421212a67711c3b3cef04a2e3c/parse_ranges/parse_ranges.py)

There's no way I did this the way it's supposed to be done, but I wanted to see what I could do without using the hints. I can't wait to see how this is supposed to actually be solved.

## What I learned from the Trey's official solution

When comparing my Base solution to Trey's official solution for the Base, I'm happy to say that I more or less have the same solution. The biggest thing I could have done to make it more pythonic was to not create a variable just to store the split.

Instead of 

```python
ranges = string.split(',')
    iterable = []
    for item in ranges:
```

I could have done

```python
iterable = []
    for item in ranges.split(','):
```

His first solution is more Pythonicly naive in that I'm doing a range while he's doing a while loop. His second solution is almost exactly my code. The only difference is that he uses multiple assignment so that he can have start and stop of the range as variables rather than referring to the loop variable. He also mentions that a list comprehension as written would be complicated which mirrors my experience that trying to rewrite this as a list comprehension was a real pain in the butt. That said, even when it's all said and done, he still has two list comprehensions, not one. And he then turned one of them into a generator because if you're only going to loop once, you should use a generator. That leads to:

```python
def parse_ranges(ranges_string):
    """Return iterable based on comma-separated numeric ranges."""
    pairs = [
        group.split('-')
        for group in ranges_string.split(',')
    ]
    numbers = [
        num
        for start, stop in pairs
        for num in range(int(start), int(stop)+1)
    ]
    return numbers
```

As for his bonus 2, it's interesting he doesn't like the solution that would give him the same as my solution (only with generators and list comprehensions).

```python
def parse_ranges(ranges_string):
    items = (
        group.split('-')
        for group in ranges_string.split(',')
    )
    return (
        num
        for item in items
        for num in range(int(item[0]), int(item[-1])+1)
    )
```

He finds it counter-intuitive, but I feel the complete opposite; I find it more intuitive. He talks about using partitions which leads him to a completely different bonus 3 answer than I got. That said, his bonus 3 answer is actually pretty darned readable:

```python
def parse_ranges(ranges):
    for group in ranges.split(','):
        start, sep, end = group.partition('-')
        if end.startswith('>') or not sep:
            yield int(start)
        else:
            yield from range(int(start), int(end)+1)
```