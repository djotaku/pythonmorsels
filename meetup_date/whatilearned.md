# What I Learned

I've worked with datetime before, but it is by no means a module I've memorized or internalized. I am looking forward to learning more here. (Or at least cementing some concepts)

## Base Problem

[My Base Solution](https://github.com/djotaku/pythonmorsels/blob/4723871e76cf69cbcf0b8ede7e42b966badc3be5/meetup_date/meetup_date.py)

My first inclination was to use the Calendar module. Its method itermonthdays4 seems to return exactly what we need - a datetime.date object. However, after playing with that for about half an hour, I couldn't quite get it to do what I needed. After that I decided to start off with a naive attempt at the problem to see if a better solution presented itself.

So, interestingly, Trey says it will be tricky with just datetime, but I found it SO MUCH easier than what I was trying to do with calendar. I'll be VERY interested in seeing what his solution is!

## Bonus 1

[My Bonus 1 Solution](https://github.com/djotaku/pythonmorsels/blob/7c482e6187a6cf6cecee6f69b8c48ddb85a6b3ca/meetup_date/meetup_date.py)

Bonus 1 was extremely easy. All I had to do was un-hardcode a few values. I suspect with bonus 2, things might get a bit trickier.

## Bonus 2

OK, things are getting ridiculous here. There is no way this is the right way to solve this - it's bonkers. But it works! Which, I think is the whole reason I'm doing these exercises. To learn the more elegant ways to program in Python.

## Bonus 3



He said object, not class, so I'm guessing maybe a named tuple or extended dictionary? Looks like I was right. A namedTuple with default values turned out to provide a working solution for Bonus 3. However my code is bananas. Let's see what Trey actually recommends. 

## Trey's Solution