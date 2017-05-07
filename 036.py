"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

from util import is_palindromic

# THOUGHTS:
#
# We are only interested in odd numbers (if have to start with 1, has to end
# with 1). Instead of check every number until one million if they are
# palindromic in both bases, create palindromic numbers in one base and check
# in the other. Maybe it's easier to build the number in base 10 and check in
# base 2.


def solve(n):
    s = 0
    for i in range(n):
        if is_palindromic(i, 10) and is_palindromic(i, 2):
            s += i
    return s

if __name__ == "__main__":
    print(solve(1000000))
