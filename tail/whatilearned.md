# What I learned

## Base Problem

[Base Problem and Bonus 1 Solution](https://github.com/djotaku/pythonmorsels/blob/f77e145739b2cd54097d7ae5e9b7e58bd05109ac/tail/tail.py)

This wasn't too hard for me as I knew about slices. Now, I don't often slice from the back, so I had to play around a little in the REPL to confirm I had the right syntax.

## From Bonus 1

As part of dealing with the 0 constraint, I ended up solving Bonus 1. I wonder if I'll discover a more elegant solution to the base when Trey sends out the solutions email.

[Base Problem and Bonus 1 Solution](https://github.com/djotaku/pythonmorsels/blob/f77e145739b2cd54097d7ae5e9b7e58bd05109ac/tail/tail.py)

## From Bonus 2

I learned about deques. They're really neat lists where you can limit the max size of it and it automatically throws away items as it fills.

[Solution To Bonus 2](https://github.com/djotaku/pythonmorsels/blob/33f6a214cfeaf5c76bd8369bb623b3ab04da5aa1/tail/tail.py)

## What I learned from Trey's Official Solution

I could have just done list(deque(iterable,maxlen=n)) instead of using the for-loop to make the deque.