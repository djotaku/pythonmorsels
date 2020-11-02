# What I Learned

## Base Problem

For this problem I wanted to record how I was solving this step by step. I know that, to be Pythonic, I want to use list comprehension. But since I'm still building up intuition, I start it off this way and then build a list comprehension. So here's the solution before I did the list comprehension. As a bonus, this ends up passing bonus 2 already. 

[Before List Comprehension](https://github.com/djotaku/pythonmorsels/blob/28110d0df160971eb99e0190ba198127152f30dd/uniques_only/uniques.py)

As I tried to do list comprehension, I figured realized that the way I solved this problem required a the deduped_list to already exist in order to compare against it. Maybe this needs a lambda expression?

## Bonus 1

For bonus 1 I thought that I just had to change the code to have yield from deduped_list. But that did not work. I may be confusing iterator and iterable. So I went to the hint: [How to make an iterator in Python](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/), which I believe I've been to for past Python Morsels.

## Bonus 2

Solved by my base problem solution.

## Bonus 3

## What I learned from Trey's Solution