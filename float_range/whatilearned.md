# What I Learned

## Base Problem

[Base Solution](https://github.com/djotaku/pythonmorsels/blob/e86192c0a014745946be2033705021ca1d343f6e/float_range/float_range.py)

I believe I could easily implement a generator function by going back through my notes from previous Python Morsels exercises (the first time I truly learned about, and how to use, generators). And if I were implementing this on my own, I think I know how I'd do it as a class - I'd use yields instead of returns. But I'm not sure how I'd create a class that just works the way Trey asks things to work - not calling any functions, just returning values. Maybe by implementing a return in the init? So I decided to check the callables hint he has listed. Following that link, I learned that a callable is essentially anything we call with parenthesis is a callable - including functions, classes, class methods, and instances of classes. Ah, midway through the page I found out that what I need to make a class callable is to add a dunder call method.  That got me to [this point](https://github.com/djotaku/pythonmorsels/blob/e7f21e709e6e34d9411b0f5756ed16df245352d5/float_range/float_range.py), but I wasn't sure what to put into the call method. So it was on to the next hint link. Unfortunately, that was a function hint, not a class one. None of the rest of the hints were involved in where I was having an issue. So I went off to Google. After looking at https://www.geeksforgeeks.org/__call__-in-python/, maybe what was throwing me off was the kwargs part? Nope, I still didn't understand. Eventually I got [here](https://github.com/djotaku/pythonmorsels/blob/19be840afc6fd93be32d9d53aabc65f1f825dc31/float_range/float_range.py) after a bit more Googling. But it wouldn't stop. Well, it wouldn't go any higher than 2.5, but it would keep printing 2.5 over and over, infinitely. So eventually I came across [this page](https://www.w3schools.com/python/gloss_python_iterator_stop.asp) and figured out what I needed to do. At that point it was time to deal with some unit tests that hadn't been called out in the instructions. I thought I understood optional arguments - you just provide defaults. But...apparently not. 

Eventually I figured it out, I needed to use * and then a parameter name. (Different from ** which means keyword arguments) But the weird that that happened is that I was getting errors where it apparently was using dunder call, but then going to my init params. That's where I had to have:
```python
self.stop = parameters[0]
```

Once I did that, I had a base problem that passed. (But I added it to dunder call for consistency, too)

## Bonus 1

Time to implement dunder len. I knew that was what I had to do, what I didn't know was how to implement it. I checked the proffered link and that didn't help since I already knew I needed to do a dunder len. I had to give up on this one from not being able to find what I needed via Google.

## Bonus 2

I thought I had the right idea, but as with len above, I had no idea what to return.

## Bonus 3

I didn't even try here.

## What I learned from Trey's Solution

The solution I came up with for the various argument requirements was along Trey's road towards the right solution, but he regards it as inelegant. I agree. But I wasn't sure what to do because it appeared that I had to have stop be the second argument and ALSO be able to take in only stop as an argument. Here's what he does to make it more elegant:
```python
def float_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
```
It took me a minute to wrap my head around this, but what he's doing is using multiple assignment to say that if nothing was supplied but the start, assign start to 0 and assign stop to the value that would have been assigned to start and assign it to stop.

When he moved on to bonus 1, some interesting things here:

First of all, he has all the math in the dunder iter method rather than using dunder next. I wonder why that is. I'm pretty sure I did it via dunder next because of one of the examples. Maybe it's because he's using a generator rather than a return? Second, the math behind dunder len is something I should have thought of, but wasn't thinking about this problem mathematically. It is:

```python
return max(ceil((self.stop-self.start) / self.step), 0)
```
So, basically, you're figuring out how many numbers between the start and stop of the generator. Then you're dividing by the number of steps you need to take. Brilliant!

For Bonus 2, I was going along the right track, but I didn't go far enough. I needed to just do the opposite of what I had in next - or what should have been in dunder iter with yields.

Bonus 3 quickly got pretty complex, but the clearest way to do it for my level of understanding was:

```python
def __eq__(self, other):
        if isinstance(other, (float_range, range)):
            if len(self) == len(other) <= 1:
                return list(self) == list(other)
            my_vals = (next(iter(self)), next(reversed(self)), self.step)
            other_vals = (next(iter(other)), next(reversed(other)), other.step)
            return my_vals == other_vals
        else:
            return NotImplemented
```
