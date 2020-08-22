# What I learned

## Base Problem

[Base Solution](https://github.com/djotaku/pythonmorsels/blob/42c02a8e0b2665f6a9d49f8860bbd34b3e67ea77/point/point.py)

Base problem was pretty easy. I got it in one because I've already done all of this before for my other projects, particularly the equals comparison and the repr function. I bet I could have done it neater using dataclasses, but I wanted to do it as best I could without looking anything up.

## Bonus 1

[Bonus 1 Solution](https://github.com/djotaku/pythonmorsels/blob/bbce2f4163a20e6f5c1e5f6511df12b0fc63aacf/point/point.py)

I took a wild guess that if there was __eq__ then there would probably be __add__ and __sub__ and I was right.

## Bonus 2

[Bonus 2 Solution](https://github.com/djotaku/pythonmorsels/blob/d3dc46deeb189e3c0ef27143dd1bba19642a8c46/point/point.py)

For multiplication, I didn't think it would follow the same pattern because he didn't have us multiplying points (which I think would have maybe been matrix math?) Instead he has us multiplying by a scalar. So I wasn't sure at first where to go. I decided to check the hints. So I needed __rmul__ instead of __mul__ as I suspected. Tricky, tricky, Trey! And yet even trickier, because it turns out that the code above is not 100% right. It works if you have 2*Point. But if you have Point*2, it fails. So I actually did have to implement __mul__. This does mean that I would need to do some sanitization on the code if I wanted to be able to do a dot product. For the correct answer - see the Bonus 3 solution and look at __mul__.

## Bonus 3

[Bonus 3 Solution](https://github.com/djotaku/pythonmorsels/blob/2fc99d0badfdf38108b904c61373940458645abd/point/point.py)

For this particular problem, here is where I truly learned something. I didn't even have the first clue of what I needed to do to solve this bonus. So, off to hints land! This comes together with everything I've been learning so far with Trey and ties nicely with all the iteration, iterator, etc stuff he's been having us do! The solution is to do __iter__ and create a generator that gives the answers.

## After Reading Trey's Official Solution

This is one of the exercises that works really well to me as the proof of why Python Morsels is a really awesome exercise for improving the understanding of Pythonic code. As I said above - the algorithmic answer was easy. But it was not the best, most Pythonic code. Let's take a look at what I can change based on his official solution for the base problem.

