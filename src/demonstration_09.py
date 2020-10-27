"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""


def is_even(n: int) -> bool:
    # use the % modulo operator to determine if even or odd
    return n % 2 == 0


def get_middle(input_str):
    # Your code here
    # how do we determine lenght of string is even or odd
    # figure out how to get char or chars
    # return the single middle char if the lenght of string is odd
    # return 2 middle chars if length is even
    length = len(input_str)
    midpoint = length//2
    if length <= 2:
        return input_str
    elif is_even(length):
        return input_str[midpoint - 1:midpoint + 1]
    else:
        return input_str[midpoint]


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
