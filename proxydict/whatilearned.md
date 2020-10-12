# What I Learned

## Base Problem

[Solution for Base, Bonus 1, and Bonus 3](https://github.com/djotaku/pythonmorsels/blob/7c309633d722ab29ee89f2609dc5c00980767104/proxydict/proxydict.py)

At first I was quite a bit lost. Then I thought perhaps I need to use abstract base classes, but I couldn't remember what they were called. So I clicked on the first hint. I was right and I was reminded of the term "abstract base class". This was not sufficient in itself for there was not a Dictionary in collections.abc. So after looking at the table in https://docs.python.org/3.8/library/collections.abc.html#module-collections.abc for a while, I thought Collection would give me a lot of what I wanted. But it was still missing a bit, so I looked at mapping, which was probably the best thing to use because it was immutable and inherited from collection. This is a very, very esoteric part of Python, but it was interesting to learn how to implement an ABC; particularly the fact that it will let you know which dunder methods you're missing when you try to create a class

## Bonus 1

[Solution for Base, Bonus 1, and Bonus 3](https://github.com/djotaku/pythonmorsels/blob/7c309633d722ab29ee89f2609dc5c00980767104/proxydict/proxydict.py)

Completing the Base Problem also gave me the bonus 1 solution. Hmm... I wonder if he created this with an older version of Python. I'm not sure why my solution passes these tests.

## Bonus 2

[Solution for Bonus 2](https://github.com/djotaku/pythonmorsels/blob/d75bf1e79cea691095ed6c3c522583706f7b457b/proxydict/proxydict.py)

I don't think I have the prettiest syntax for my repr method, but I left in (commented out) how I was trying to be elegant and use a list comprehension. I think at this point, I would need a lambda or something to have that if/else in a list comprehension. At any rate, it passes the tests now! Woohoo!

## Bonus 3

[Solution for Base, Bonus 1, and Bonus 3](https://github.com/djotaku/pythonmorsels/blob/7c309633d722ab29ee89f2609dc5c00980767104/proxydict/proxydict.py)

Completing the Base Problem also gave me the bonus 3 solution. As with bonus 1, I'm not sure if he's using an older version of the library or something. I don't feel my barebones solution should have solved both of these. 

## What I learned from Trey's Solution

Boy, oh boy is there a lot to learn here. Looks like the reason I had 1 and 3 already done for me is that I jumped the gun on ABC vs his more naive solution, which is what I was trying to do before I thought about ABC (but couldn't remember what it was called) and looked at his hint. (Basically, if I could have intuited getitem method, I would have probably also started out with this naive method).

The biggest bombshell Trey drops is that there standard library already includes types.MappingProxyType so if you do:

```python
from types import MappingProxyType as ProxyDict
```

You're already done with the base solution. 

For bonus 2, there are two things to cover: iter and repr.

Thanks mostly to Trey's problem sets I knew that I wanted to use yield or that I probably wanted to do a generator. So I thought my solution was pretty good. As a reminder:

```python
    def __iter__(self):
        return (key for key in self.proxy_dictionary.keys())
``` 

but it turns out there are two simpler things I could have done. Since I'm proxying a dict, which already has an iter method, I could have done:

```python
def __iter__(self):
        yield from self.proxy_dictionary
```
or I could have done
```python
    def __iter__(self):
        return iter(self.proxy_dictionary)
``` 

I actually think the first one is more readable. For the repr I kept thinking there must be some easier way to do this. Because the dictionary already has a repr. But I thought that would result in something like ProxyDict(dict(stuff)); apparently not. Because this is Trey's solution:

```python
def __repr__(self):
        return f"ProxyDict({repr(self.proxy_dictionary)})"
```  
Although, that locks in the class name and causes issues if someone wants to do the same thing with our class. So the better way is:

```python
def __repr__(self):
        return f"{type(self).__name__}({self.proxy_dictionary!r})"
```

the !r is the same as repr(self.proxy_dictionary)