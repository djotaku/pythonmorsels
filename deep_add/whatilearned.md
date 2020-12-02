# What I learned

## Base Problem

[Link to Base Solution](https://github.com/djotaku/pythonmorsels/blob/4af071b8eb4053e8c0ef6638d7ad7b42c0fa2986/deep_add/deep_add.py)

I thought there must be a way to collapse these lists. I thought about zip, but that's not it. If it's accumulate, I gave up before figuring out how to make it go. I'm pretty sure there's something and I just couldn't remember what it was. So I came up with this recursive solution. I'm pretty sure I'm going to slap my head when I read Trey's solution.

## Bonus 1

[Bonus 1 Solution](https://github.com/djotaku/pythonmorsels/blob/69c1f47fab6412dbec8d328ce59ec543c80e127e/deep_add/deep_add.py)

This one wasn't too hard. I just had to change my check of list to Iterable.

## Bonus 2 

[Bonus 2 Solution](https://github.com/djotaku/pythonmorsels/blob/7c1de27949c3f77570a0e7727b1e0d2e56edc142/deep_add/deep_add.py)

This one was EXTREMELY EASY. Like...too easy! I wonder what Trey's solution will be like.

## Bonus 3

[Bonus 3 Solution](https://github.com/djotaku/pythonmorsels/blob/e0bc4fbc74005d5fc6a7d8f3eb8c599074fc98d4/deep_add/deep_add.py)

This one took a bit of thinking. But, ultimately it wasn't too hard once I stepped away and came back to it. Basically, instead of just adding the start value at the end, I had to pass it in so that once I was in the function it could become a timedelta instead of 0. 

## Trey's Solution

First of all, I'm happy that Trey's original solution wasn't any more elegant than mine. That is to say, recursion is the solution and there isn't some built-in for this. Also, I was RIGHT! There is a way to make the math a little more automated. Trey's ultimate solution (where he went more elegant by making it a generator comprehension) is:

```python
def deep_add(list_or_number):
    """Return sum of values in given list, iterating deeply."""
    if type(list_or_number) == list:
        return sum(deep_add(x) for x in list_or_number)
    else:
        return list_or_number
```

Huh! For bonus 2 I'm really surprised Trey chooses to flip things around in the if statement rather than checking if it's an Iterable. Turns out he does it for bonus 3. So it's one of those things where the way my brain works meant I was prepared for future bonuses while working on prior ones. This one was pretty fun, even if I was a little stumped at first until I got the recursion going.