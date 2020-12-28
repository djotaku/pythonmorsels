# What I Learned

## Base Problem
I believe I could easily implement a generator function by going back through my notes from previous Python Morsels exercises (the first time I truly learned about, and how to use, generators). And if I were implementing this on my own, I think I know how I'd do it as a class - I'd use yields instead of returns. But I'm not sure how I'd create a class that just works the way Trey asks things to work - not calling any functions, just returning values. Maybe by implementing a return in the init? So I decided to check the callables hint he has listed. Following that link, I learned that a callable is essentially anything we call with parenthesis is a callable - including functions, classes, class methods, and instances of classes. Ah, midway through the page I found out that what I need to make a class callable is to add a dunder call method.  That got me to [this point](https://github.com/djotaku/pythonmorsels/blob/e7f21e709e6e34d9411b0f5756ed16df245352d5/float_range/float_range.py), but I wasn't sure what to put into the call method. So it was on to the next hint link. Unfortunately, that was a function hint, not a class one. None of the rest of the hints were involved in where I was having an issue. So I went off to Google. After looking at https://www.geeksforgeeks.org/__call__-in-python/, maybe what was throwing me off was the kwargs part? Nope, I still didn't understand.

## Bonus 1

## Bonus 2

## Bonus 3