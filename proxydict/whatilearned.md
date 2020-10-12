# What I Learned

## Base Problem

At first I was quite a bit lost. Then I thought perhaps I need to use abstract base classes, but I couldn't remember what they were called. So I clicked on the first hint. I was right and I was reminded of the term "abstract base class". This was not sufficient in itself for there was not a Dictionary in collections.abc. So after looking at the table in https://docs.python.org/3.8/library/collections.abc.html#module-collections.abc for a while, I thought Collection would give me a lot of what I wanted. But it was still missing a bit, so I looked at mapping, which was probably the best thing to use because it was immutable and inherited from collection. This is a very, very esoteric part of Python, but it was interesting to learn how to implement an ABC; particularly the fact that it will let you know which dunder methods you're missing when you try to create a class

## Bonus 1

Completing the Base Problem also gave me the bonus 1 solution. Hmm... I wonder if he created this with an older version of Python. I'm not sure why my solution passes these tests.

## Bonus 2



## Bonus 3

Completing the Base Problem also gave me the bonus 3 solution. As with bonus 1, I'm not sure if he's using an older version of the library or something. I don't feel my barebones solution should have solved both of these. 

## What I learned from Trey's Solution