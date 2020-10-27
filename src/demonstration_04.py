"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.
"""


def emotify(txt):
    replaceable = {'smile': ':D', 'grin': ':)', 'sad': ':(', 'mad': ':P'}
    split_sentence = txt.split()
    split_sentence[-1] = replaceable[split_sentence[-1]]
    return ' '.join(split_sentence)


print(emotify("Make me smile"))
print(emotify("Make me grin"))
print(emotify("Make me sad"))
