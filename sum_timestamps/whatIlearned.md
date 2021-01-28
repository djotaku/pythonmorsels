# What I learned

## Base Problem

[My Solution to the Base Problem](https://github.com/djotaku/pythonmorsels/blob/d083f27e1d1b521b10261bb891d1afd9e75eaf3b/sum_timestamps/sum_timestamps.py)

Boy, oh boy. This could have been SOOOO useful when I was compiling playtimes for my End of Year video game blog post. I will definitely be repurposing this code!

This part wasn't too hard. I'm pretty sure the fact that I loop twice means I didn't choose the most efficient way to do this, although I'm proud of my list comprehension up front. I'm guessing the absolute easiest (and maybe most elegant?) way to do this probably involves importing datetime and having that do the math for you. I'm curious to see what Trey does for this answer.


## Bonus 1

[My Solution to the 1st Bonus](https://github.com/djotaku/pythonmorsels/blob/fabf32e4ca5cefe828f3b0b4ddd68c598a208c56/sum_timestamps/sum_timestamps.py)

For this part, the fact that I have to check for 60 twice makes me thing I should refactor that out to a function. I did so and it made things pretty easy. Again, if you look at my code, it's starting to get a bit messy. I'm very sure at this point that Trey is going to have a much cleaner solution.

## Bonus 2

[My Solution to the 2nd Bonus](https://github.com/djotaku/pythonmorsels/blob/cfb6182561c9801c4247bfecafd47f0cc465a4e3/sum_timestamps/sum_timestamps.py)

This seemed a bit tough at first, but it actually wasn't too hard. This whole time, I've had the feeling that I've been doing this in the most inelegant way possible. I feel it strongest here. Still, I was able to finish this exercise in about 20 minutes, so that's pretty neat. 

## What I learned from Trey's Solution

Interestingly, using time from datetime is only one of MANY solutions that Trey presents. This problem truly has multiple solutions which work and have varying levels of elegance. There are even some that he remarks are cleverer, but less readable. And, in Python (probably all languages), we want to prefer readability and understanding over clever code. And, it turns out that I was a little quick to be a little too clever and that led to my code having 2 loops when it could have just had one.

This is his first solution and the one closest to mine.

```python
def sum_timestamps(timestamps):
    total_time = 0
    for time in timestamps:
        minutes, seconds = time.split(':')
        total_time += int(minutes) * 60 + int(seconds)
    minutes = total_time // 60
    seconds = total_time % 60
    if seconds < 10:
        return f"{minutes}:0{seconds}"
    else:
        return f"{minutes}:{seconds}"
```

You see, he's able to just do it all in one loop. He also just sums all time and then does the division and modulo. This saves all sorts of variables and is just much clearer. From something else, I think Advent of Code, I'd remembered there was a way to get the division and remainder in one step, but I didn't feel like looking it up. It's called divmod and it changes the answer to:

```python
def sum_timestamps(timestamps):
    total_time = 0
    for time in timestamps:
        minutes, seconds = time.split(':')
        total_time += int(minutes) * 60 + int(seconds)
    minutes, seconds = divmod(total_time, 60)
    return f"{minutes:01d}:{seconds:02d}"
```
Trey then went through a bunch of other solutions. Sign up for a free trial or pay his subscription fee to see those.

His bonus 1 is actually really close to my answer to bonus 1! Just replace my division and modulo with divmod. It always makes me feel happy when Trey and I have the same solution.

Once again, his first solution is like mine - only he uses a Try/Except instead of an if/else.

His preferred solution involves regular expressions, but I say to that - "if you try to solve a problem with regular expressions, now you have two problems." I kid, somewhat. But this one is particularly cryptic to me and not quite as parse-able if I came back to it in a few months.

