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

For this one I just went ahead with the hint because in the past (before Python 3.x and its embrace of UTF-8) I'd dealt with this by just dropping the non-latin characters. 