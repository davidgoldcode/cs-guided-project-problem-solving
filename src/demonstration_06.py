"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


# def get_count(input_str: str) -> int:
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for i in range(len(vowels)):
#         count += input_str.count(vowels[i])
#     return count

def get_count(input_str: str) -> int:
    num_vowels = 0
    vowels = 'aeiou'
    for char in input_str:
        if char in vowels:
            num_vowels += 1
    return num_vowels


print(get_count('hello'))
print(get_count('abcdeeeef'))
