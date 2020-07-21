# What I learned

## From Bonus 1

I learned about @property which allows you to access a method as if it were a property of a class. At least in this example and the example YouTube video linked, the main benefit was being able to refactor without downstream code having to change.

## From Bonus 2

How to use @method_name.setter. I wonder if I could stack this with the @property decorator or if this is dependent upon overloading the method. Hopefully Trey's explanation of the solution will provide some edification there.

## From Bonus 3

This one was TOUGH. I spent over an hour trying to figure it out. I couldn't just adapt what I did for Bonus 2 because it would end up causing recursion. So the trick I learned wasn't linked in Trey's hints. It was here: https://www.programiz.com/python-programming/property . Basically you can do self._radius in init. Then you create the radius method and that will reference the variable name from the init.