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

[My Bonus 2 Solution](https://github.com/djotaku/pythonmorsels/blob/56598b95c000026c340242057678a97b838608c9/meetup_date/meetup_date.py)

OK, things are getting ridiculous here. There is no way this is the right way to solve this - it's bonkers. But it works! Which, I think is the whole reason I'm doing these exercises. To learn the more elegant ways to program in Python.

## Bonus 3

[My Bonus 3 Solution](https://github.com/djotaku/pythonmorsels/blob/4f5da61df2d4e6ebf030a7ed36a91df2f2d34756/meetup_date/meetup_date.py)

He said object, not class, so I'm guessing maybe a named tuple or extended dictionary? Looks like I was right. A namedTuple with default values turned out to provide a working solution for Bonus 3. However my code is bananas. Let's see what Trey actually recommends. 

## Trey's Solution

So it looks like my intuition to use the Calendar module was correct. For almost every solution, except Bonus 1, he mentions that the Calendar module is the easiest and/or more readable. And a big focus on these exercises is not just to make things more elegant or Pythonic, but to make them more readable and maintainable. At one point I also thought of using a generator, but having gotten stuck with the Calendar module, I had already decided to go on the naive route. This is one of the rare times where I'm not sure if I prefer my solution or Trey's solution more in terms of understanding what it does as well as adaptability. It was very easy to adapt mine without needing to create helper functions. I just moved from magic values to variable names. But near the end Trey ends up having to create helper functions.

For example, this is his first solution:

```python
from calendar import Calendar, weekday, THURSDAY

def meetup_date(year, month):
    """Return a date of the fourth Thursday of the given month."""
    nth = (
        4
        if weekday(year, month, 1) != THURSDAY
        else 3
    )
    thursday_calendar = Calendar(THURSDAY).monthdatescalendar(year, month)
    return thursday_calendar[nth][0]
```
Essentially he's saying that if first day of the month is a Thursday, then you want the 3rd week of a calendar that has Thursday as the first day of the week (instead of Sunday or Monday). Otherwise, you want the fourth week. This is why things get tricky in bonus 2 when you can count backwards and there are sometimes 5 weeks in a month. With my solution, it doesn't matter, we're just counting calendar days and figuring out if we've reached the right Thursday yet. 

However, you can't deny the Pythonic-ness of his Bonus 2 solution, even if it takes a bit more to understand.

```python
from datetime import date
from calendar import monthcalendar, THURSDAY

def weekdays_in_month(year, month, weekday):
    """Return list of all 4/5 dates with given weekday and year/month."""
    return [
        date(year, month, week[weekday])
        for week in monthcalendar(year, month)
        if week[weekday] != 0
    ]

def meetup_date(year, month, *, nth=4, weekday=THURSDAY):
    """Return date of the nth weekday of the given month."""
    return weekdays_in_month(year, month, weekday)[nth-1 if nth > 0 else nth]
```

Basically, he's using a helper function that puts all the Thursdays in a month into a list via list comprehension. Then he just uses list index (hence the need to subtract 1 from nth since lists start counting from 0). It's pretty genius!  

As for Bonus 3, I guess a class would have been fine. But at least I learned about using namedTuples.