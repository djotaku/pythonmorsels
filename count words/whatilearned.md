# What I learned

## Base Solution

[Base Solution](https://github.com/djotaku/pythonmorsels/blob/0e457f8350cd822c5bd6d2f282b2259f16fea153/count%20words/count.py)

So, for this one, I had done something similar in Impractical Python. I didn't actually end up committing the solution that contained what I needed, but I knew it was in collections. So, as Trey said, I didn't got to Google or Stack Exchange. I just looked in the Python docs for collections, since I knew it was there. Actually, at first I thought maybe itertools? Like iterate and accumulate. But accumulate is something else.

Then, once I had the right package, my first attempt at the solution actually broke out the sentence into letters. I wanted WORDS. But I've been doing Python for a long time, so I knew about split. Once I had that, it was easy to get the base solution. 

## Bonus 1

[Bonus 1 Solution](https://github.com/djotaku/pythonmorsels/blob/9abc1b34a8f613009c4cbd23071cc2d780b9a6b8/count%20words/count.py)

Once again, I knew about lower. But I was pleasantly surprised that I could chain that with split rather than have to update the variable twice.

## Bonus 2

[Bonus 2 Solution](https://github.com/djotaku/pythonmorsels/blob/b2f11a7d05b30baf43c39bed164b7fa4ba52f96f/count%20words/count.py)

My initial guess was that Bonus 2 would probably hinge around regular expressions. But I clicked on the hint link to see if there was some cool built-in function of strings. Turns out I was right! I was having issues with it splitting up "don't" So I had to setup the regular expression to only look for special characters at the beginning and end of a word. The solution I came up with took me a while to get the regular expression working. It's definitely not elegant, so I'm very curious to see what his solution ends up being.

## What I learned from Trey's Solution

This time, while I was able to get the solution and bonus 1 pretty easily, it turns out that my code was more verbose than it needed to be. The only confusing part about his solution is that he claims I could just do "split" without the stuff I have in the parenthesis. I wonder why it didn't seem to work for me. That aside, what's interesting is that, just like deque last week, I don't actually need to make use of a for-loop. The Counter function will auto-iterate for me. (Which is weird, because the documentation shows a for-loop, but maybe that's just to make things more clear?) 

A more important thing is the Regular Expression part (I really should start going through at least one of my many RE books from O'Reilly). Instead of trying to eliminate the prefix and suffix punctuation, I should have just done:

```
r"\b[\w'-]+\b"
```

This means look for words, apostrophes, and dashes and get rid of whatever's outside the word. So this gets by the problem I was having at first with the word "don't"

So here is the final solution - a mashup of my code and Trey's:

[After Trey's Solution](https://github.com/djotaku/pythonmorsels/blob/536dbd42077857d9ed00408988d415e3cab41c20/count%20words/count.py)