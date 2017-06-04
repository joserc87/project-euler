"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

import functools
import operator
import util


def til(n):
    """ Silly function to generate all the digits for testing """
    return ''.join([str(l) for l in range(1, n+1)])

# THOUGHTS:
#
# digigs | # numbers        | length
# -------+------------------+---------
#      1 | 9                | 9
#      2 | 99 - 9 = 90      | 90*2
#      3 | 999 - 99 = 900   | 900*3

# digits | Range (from | to)
# -------|------------------
#      1 | 1|9
#      2 | 9+1|9 + 90*2
#      3 | 189+1|189 + 900*3

# TEST:
# assert len(til(9)) == 9
# assert len(til(99)) == 9 + 90*2
# assert len(til(999)) == 9 + 90*2 + 900*3


def get_range_digits(n):
    """ Gets the range (l, h) where l is the position of the first number with n
    and h is the last digit of the last number that has n digits"""
    if n == 1:
        return (1, 9)
    else:
        l0, h0 = get_range_digits(n-1)
        l = h0 + 1
        h = h0 + 9*(10**(n-1))*n
        return (l, h)
# TEST
# assert get_range_digits(3) == (190, 189 + 900*3)


def d(p):
    # Find the range + number of digits:
    num_digits = 1
    range_digits = None
    while range_digits is None:
        l, h = get_range_digits(num_digits)
        if l <= p and p <= h:
            range_digits = (l, h)
        else:
            num_digits += 1

    # Find the digit inside that range:
    l, h = range_digits
    rel_pos = p - l
    first_number = 10**(num_digits-1)
    number = rel_pos // num_digits + first_number
    rel_digit = rel_pos % num_digits

    # Get rel_digit digit of number
    digits = util.get_digits(number)
    return digits[rel_digit]
# TEST
# assert ''.join(str(d(i)) for i in range(1, get_range_digits(3)[1] + 1)) == \
#     til(999)

if __name__ == '__main__':
    l = [d(10**p) for p in range(7)]
    s = functools.reduce(operator.mul, l, 1)
    print(s)
