# What I Learned

## Base Problem

[Base Problem Solution](https://github.com/djotaku/pythonmorsels/blob/9a699f874489aa1b1ef40785d3f41545105a247a/is_perfect_square/perfect_square.py)

Trey began his problem statement this way: "This week I want you to write a function that might seem simple at first, but there's a number of ways to solve it." It definitely took some out of the box thinking for me to figure out how I was going to solve the base case. The math.sqrt() function returns a float so that it can give answers for non-perfect squares. So I kept thinking and I realized that any perfect, non-complex square root must be an integer. So I came up with the conditional to return. (And after all this Pythonic learning, I've learned not to evaluate for truth and then return a variable. Just return the evaluation)
## Bonus 1
[Bonus 1 Solution ](https://github.com/djotaku/pythonmorsels/blob/9546bbdf74ca1675c9335d48d99440148f167bc5/is_perfect_square/perfect_square.py)
Bonus 1 was trivial. Anyone who's done any amount of functional programming could figure it out.
## Bonus 2

[Bonus 2 Solution](https://github.com/djotaku/pythonmorsels/blob/15a1754bc6bd1356db9ea5ac131927091e720339/is_perfect_square/perfect_square.py)

He mentioned in his intro that the second two bonuses would be hard. I think I can probably reason my way to a solution for bonus 3. I'm quite a bit rusty on complex numbers, but I think I can get my mind to remember. (Despite having an electrical engineering degree, I've rarely had to use it. Ended up becoming a programmer and then a boss in a programming shop) For this one, however, I had no idea why Python couldn't deal with large numbers. After all isn't Python the current darling of the scientific community now? So I clicked on the [first link related to this hint](https://stackoverflow.com/a/47854670/2633215). The Decimal answer didn't work. I wasn't ready to do gmpy2 yet. So I clicked on the [second link](https://pymotw.com/3/decimal/#local-context). Looked like Decimal was probably most likely the way he wanted me to go. That, of course, created some issues with 0.0 not being equal to 0, so I had to change things. I spent about 15-20 minutes trying to figure out if there was a Decimal way to get the integer part separated from the part after the decimal. Tragically, no. I *did* discover math.modf which will do that for you. However, it was not operating under the same context as the Decimal, so it was rounding too small that to work. (What I was trying to do there is that any perfect square should have nothing to the right of the decimal point.) Eventually, I had the thought that almost the same as the base and bonus 1, just "phrased" slightly differently. If I was previously seeing if they were both the same number, then I could move it over to this side of the equation and ask if sqrt(a)-int(sqrt(a))=0. I finally had a working solution once I raised the context high enough to get enough decimal places for that to work.
## Bonus 3

[Bonus 3 Solution](https://github.com/djotaku/pythonmorsels/blob/0764e69a7c100eba7c678d73671e50fc9b3d07d4/is_perfect_square/perfect_square.py)
Bonus 3 was incredibly easy, especially after bonus 2. All I had to do was a quick read of the cmath library and see that a number N that is complex has N.real and N.imag to acces the numbers in each part of the complex number. Then I just do what I did above to see if they are integers by making sure nothing's right of the decimal place. Piece of cake! Also, I already knew about kwargs from other Trey problems plus reading up on it and it FINALLY made sense after all these years of not making sense to me.

## After Reading Trey's Solution

For the base solution I was very happy to see that my solution was one of Trey's solutions! That makes me feel like I truly made progress by doing these Python Morsels exercises!! Same thing with bonus 1, but bonus 1 was a cake walk.  For bonus 2 what I learned is that I could see how large a number is to determine the precision I want. That's more for efficiency than anything else. I'm surprised Trey didn't use kwargs here and instead had the function signature look like:

def is_perfect_square(number, *, complex=False):

but if he was going to do it like that, why not eliminate the *? 