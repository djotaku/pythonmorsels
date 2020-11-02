# What I Learned

## Base Problem

For this problem I wanted to record how I was solving this step by step. I know that, to be Pythonic, I want to use list comprehension. But since I'm still building up intuition, I start it off this way and then build a list comprehension. So here's the solution before I did the list comprehension. As a bonus, this ends up passing bonus 2 already. 

[Before List Comprehension](https://github.com/djotaku/pythonmorsels/blob/28110d0df160971eb99e0190ba198127152f30dd/uniques_only/uniques.py)

As I tried to do list comprehension, I figured realized that the way I solved this problem required a the deduped_list to already exist in order to compare against it. Maybe this needs a lambda expression?

## Bonus 1

[Bonus 1 Solution](https://github.com/djotaku/pythonmorsels/blob/4625fb50e63f213b728a967dd641a5efed50bd0d/uniques_only/uniques.py)

For bonus 1 I thought that I just had to change the code to have yield from deduped_list. But that did not work. I may be confusing iterator and iterable. So I went to the hint: [How to make an iterator in Python](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/), which I believe I've been to for past Python Morsels. So it turns out I was very CLOSE. I didn't want to yield or yield from on the whole list. If I had to make it to a list, then even if I was returning an iterator, it would still have to consume the entire input. (At least I think that's the case.) Either way I'm both happy that I was on the right path and that I didn't have to change much to get to this solution.

## Bonus 2

Solved by my base problem solution.

## Bonus 3

I had to read this one a few times to really understand what was going on here. If my input iterable was something like \[1,3,4,5,5\], then it was hashable. If it was a list of lists, then it was not. Since I was never passing bonus 3 with just hashables, that leads me to believe what I already knew - I'm not doing this in the most efficient way. I want to record here that I thought about using sets somehow, but Trey wanted us to make sure we retained order and I don't think I could do that with sets. I'm going to guess that Trey's Solution is that the unhashable solution is something similar to what I came up with and the hashable one is some new, neat technique I'll be happy to have learned about. So, uncharacteristically for the Python Morsels, I will skip this bonus and go on to his solution.  

## What I learned from Trey's Solution

It was good to be vindicated in my understanding that sets won't work because they're unordered. There's a weird potential solution that involved indexes. For the most part (there are exceptions), if you're doing list comprehension or taking advantage of Python's for loops, you don't need indexes, so that never crossed my mind. Trey's third proposed solution is my solution and his only critique is that it's slow (we knew this from the failure to pass the Bonus 3 criteria). The better solution actually turns out to be a combination of the first and last solutions and that's really cool. It looks like this:

```python
def uniques_only(iterable):
    """Return iterable in the same order but with duplicates removed."""
    seen = set()
    items = []
    for item in iterable:
        if item not in seen:
            items.append(item)
            seen.add(item)
    return items
```

So basically you're comparing where we've seen it to a set rather than a list, which is faster. But you're appending to a list, so you maintain order. He also mentions a super neat solution that isn't preferred because it's less readable. (And one thing I like about Trey's solutions is that he prefers readable to clever)

```python
def uniques_only(iterable):
    """Return iterable in the same order but with duplicates removed."""
    return dict.fromkeys(iterable).keys()

```

And his Bonus 1 solution is basically the same as mine, but configured for the fact that he's using sets. Bonus 2 involves going back to my solution because it's dealing with non-hashables. That's why my first solution also worked for Bonus 2. Interestingly, the solution to bonus 3 is nothing clever or mind-bending. It's essentially using sets for hashables or lists for unhashables. So below will be my link for how I'd modify my code.

