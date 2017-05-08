"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from util import get_digits, get_int_from_digits


def it_creates_pandigital(n):
    digits = set([d for d in range(1, 10)])
    for i in range(1, 10):
        digs = get_digits(i*n)
        digs_set = set(digs)
        # If the number contains repetitions, it can't be a pandigital
        if len(digs_set) != len(digs):
            return False
        elif digits == digs_set:
            # If we have all we need, return
            return True
        dif = digits - digs_set
        # If one of the digits was already used, or if  the number contains too
        # many digits
        if len(dif) + len(digs_set) != len(digits):
            return False
        digits = dif
    return len(digits) == 0


def create_pandigital(n):
    digits = [get_digits(n*d) for d in range(1, 10)]
    digits = [j for i in digits for j in i]
    return get_int_from_digits(digits[:9])


def get_biggest_pandigital_with_n_digits(n_digits, threshold):
    for n in range(10**n_digits - 1, 10**(n_digits - 1) - 1, -1):
        if n < threshold:
            return None
        if it_creates_pandigital(n):
            return n


def solve():
    """
    The pandigital will be X*1-X*2-X*3... The largest will be based on the first
    multiplication, i.e. X. We can build pandigitals starting with one digit
    (9), then adding a digit (99, 98, 97, etc) until we find a pandigital or
    when the number gets lower than the previous pandigital.
    """
    # In general, the number of digits would be between 1 and 5, but we can't
    # make a pandigital with 5 digits that starts with any digit higher than 5,
    # so se can skip those.
    biggest = 0
    for num_digits in range(1, 5):
        candidate = get_biggest_pandigital_with_n_digits(num_digits, biggest)
        if candidate is not None and candidate > biggest:
            biggest = candidate
    return create_pandigital(biggest)

if __name__ == "__main__":
    # Some tests
    # assert it_creates_pandigital(9)
    # assert it_creates_pandigital(192)
    # assert not it_creates_pandigital(8)
    # assert not it_creates_pandigital(191)
    # assert create_pandigital(9) == 918273645
    # assert create_pandigital(192) == 192384576

    print(solve())
