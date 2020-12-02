# What I learned

## Base Problem

[Link to Base Solution](https://github.com/djotaku/pythonmorsels/blob/4af071b8eb4053e8c0ef6638d7ad7b42c0fa2986/deep_add/deep_add.py)

I thought there must be a way to collapse these lists. I thought about zip, but that's not it. I'm pretty sure there's something and I just couldn't remember what it was. So I came up with this recursive solution. I'm pretty sure I'm going to slap my head when I read Trey's solution.

## Bonus 1

[Bonus 1 Solution](https://github.com/djotaku/pythonmorsels/blob/69c1f47fab6412dbec8d328ce59ec543c80e127e/deep_add/deep_add.py)

This one wasn't too hard. I just had to change my check of list to Iterable.

## Bonus 2 

[Bonus 2 Solution](https://github.com/djotaku/pythonmorsels/blob/7c1de27949c3f77570a0e7727b1e0d2e56edc142/deep_add/deep_add.py)

This one was EXTREMELY EASY. Like...too easy! I wonder what Trey's solution will be like.

## Bonus 3

This one took a bit of thinking. But, ultimately it wasn't too hard once I stepped away and came back to it. Basically, instead of just adding the start value at the end, I had to pass it in so that once I was in the function it could become a timedelta instead of 0. 

## Trey's Solution