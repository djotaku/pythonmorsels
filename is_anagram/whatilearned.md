# What I Learned

## Base Solution

[Base Solution](https://github.com/djotaku/pythonmorsels/blob/fbc1e1a81d79a1a218448be36652afef806765c7/is_anagram/anagram.py)

Things got off to a bad start when I accidentally confused anagrams with palindromes. (Mostly because the first example almost looks like a palindrome). Wasted about an hour on that, but I did get a better understanding of various string and list functions. Once I realized it was anagrams we were after, it was pretty easy to realize you just wanted to use sets and do comparison. Unlike a list, sets don't care about order, just membership. Of course, that also meant I had to check for length as the skin, sinks test was there to remind us.

## Bonus 1

[Bonus 1](https://github.com/djotaku/pythonmorsels/blob/39ed4e589fb405254bbbf539bf398d94f5ede399/is_anagram/anagram.py)

This one wasn't too tough using replace. However, looking ahead to Bonus 2, I'm thinking regular expressions are going to be needed to keep things from getting ridiculous.

## Bonus 2

[Bonus 2](https://github.com/djotaku/pythonmorsels/blob/3cdfa6f0be6ddda810cab9c805ba331c4554b372/is_anagram/anagram.py)

I was right, regular expressions were needed here. As a bonus, it simplified things because it got rid of the need to get rid of spaces on their own.

## Bonus 3

[Bonus 3](https://github.com/djotaku/pythonmorsels/blob/744b4f11a6bf586aa7aadcd1df706cdae113fc1b/is_anagram/anagram.py)

For this one I just went ahead with the hint because in the past (before Python 3.x and its embrace of UTF-8) I'd dealt with this by just dropping the non-latin characters. With the hint, it was a cake-walk. 

## What I Learned from Trey's Solution

I knew I probably wasn't doing this to most efficient way when I did sets because I had to have the extra return False when they had different lengths. If there's one thing I've learned about Trey's problem sets, it's that they're usually much simpler than you want to do them at first. I think his solutions were actually pretty darn elegant. He offers using both Counter and sorted. Counter works because it's creating a dictionary counting up each letter and if they are equal, then they inherently have the same length. For sorted, it's basically putting the letters in order and the first time there's a duplicate (or if one is longer than the other), it'll become False.

Funnily enough, he ended up with the same bonus solutions as me. I mean, he was using Counter, but he also used replace.

I'm surprised that for his bonus 2 example, he mentions using a generator. I was explicitly trying NOT to use any kind of for loops beacuse I was certain that wasn't the solution he'd be looking for. I'm SHOCKED he doesn't do anything at all with regular expressions. Could have saved myself about an hour's worth of work just doing a for loop. 

In the end he creates 2 helper functions to help him do it. I actually almost like mine better, even if Counter is more elegant.  (First time so far that has happened with his exercises.)