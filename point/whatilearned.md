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

[After reading Trey's official solution for the base problem](https://github.com/djotaku/pythonmorsels/blob/2657eb8237455862199813b9a59ab6f9b7631609/point/point.py)

There are two important things to point out here. The one I'm less excited about is in init:

```python
    def __init__(self, x: int, y: int, z: int):
        self.x, self.y, self.z = x, y, z
```

Here Trey says we could have kept it the other way, but this way serves a function of code being its own documentation. It shows there's a relationship between the variables (they are a point in 3D space) rather than just 3 random variables.

But the one I was more excited about was the equality function:

```python
    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
```

I've gone from 3 lines to just one. I already knew from previous exercises that often when dealing with a return, an "else" is redundant. So I didn't have that in my original solution. But I always forget that you can just do something like this because if it's true, it'll cause a return true.

His Bonus 1 solution didn't provide anything I hadn't already done. Roughly the same situation for Bonus 2. Where things got really neat was in the Bonus 3 solution. The creation of __iter__ allows for a lot of neat shortcuts everywhere you're using unpacking. I didn't refactor __add__ or __sub__ so this information didn't change my code, but it was neat. As I mentioned in my base solution, I had the intuitive idea that I could use dataclasses, but I didn't have any experience with them, so I didn't bother in order to see if I could get things working without using it. So here's the solution that's the more Pythonic while eliminating a lot of boiler plate code.

