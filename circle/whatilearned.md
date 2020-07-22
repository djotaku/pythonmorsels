# What I learned

[Commit History](https://github.com/djotaku/pythonmorsels/commits/master/circle/circle.py)

## Base Problem

[Link to commit with the base problem solution](https://github.com/djotaku/pythonmorsels/blob/bbe9f111dca3d0b6cad5001b35f6515c7335a9f3/circle/circle.py)

I learned nothing. I already knew everything needed for the base problem.

## From Bonus 1

[Link to commit with the Bonus #1 solution](https://github.com/djotaku/pythonmorsels/blob/43571b5a406f3e6ae6329c4fb2a6db718ab84e08/circle/circle.py)

I learned about @property which allows you to access a method as if it were a property of a class. At least in this example and the example YouTube video linked, the main benefit was being able to refactor without downstream code having to change.

## From Bonus 2

[Link to commit with the Bonus #2 solution](https://github.com/djotaku/pythonmorsels/blob/83900a7cb1a94f41300bc2d769e35a14ecc956b5/circle/circle.py)

How to use @method_name.setter. I wonder if I could stack this with the @property decorator or if this is dependent upon overloading the method. Hopefully Trey's explanation of the solution will provide some edification there.

## From Bonus 3

[Link to commit with the Bonus #3 solution](https://github.com/djotaku/pythonmorsels/blob/dd44a8abd95bc18f4e458a5807e3ee7bfd6a7fd7/circle/circle.py)


This one was TOUGH. I spent over an hour trying to figure it out. I couldn't just adapt what I did for Bonus 2 because it would end up causing recursion. So the trick I learned wasn't linked in Trey's hints. It was here: https://www.programiz.com/python-programming/property . Basically you can do self._radius in init. Then you create the radius method and that will reference the variable name from the init.

## From Trey's Official Solution

[Link to commit with mods from Trey's official solution](https://github.com/djotaku/pythonmorsels/blob/a152d792465f77b52c670bf1488a2857034f8efa/circle/circle.py)

- It turns out I didn't need the diameter negative check (lines 26 and 27 in the [Bonus #3 solution](https://github.com/djotaku/pythonmorsels/blob/dd44a8abd95bc18f4e458a5807e3ee7bfd6a7fd7/circle/circle.py)) because the radius negative check would have handled that.

- I didn't need to make the area setter in order to raise the error. That error would have been raised simply by not creating a setter.

- I didn't need to change self.radius to self._radius in the init. Only had to use it for the @property method. 