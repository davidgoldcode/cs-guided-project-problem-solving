"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
print(last([1, 2, 3, 4, 5], 1) 
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""

from typing import List


def last(a: List[int], n: int) -> List[int]:
    if n > len(a):
        return 'invalid'
    elif n == 0:
        return [0]
    else:
        return a[(-1 * n):]


print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], 0))
