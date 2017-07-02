"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

import itertools
from util import PrimeFactory, get_digits, get_int_from_digits


def get_permutations(n):
    return [get_int_from_digits(p) for p in
            itertools.permutations(get_digits(n))]


def main():
    Primes = PrimeFactory()
    # All the primes with 4 digits
    primes4digits = [n for n in range(1001, 10000, 2) if n in Primes]
    assert 1487 in primes4digits
    assert 4817 in primes4digits and 4817 in get_permutations(1487)
    assert 8147 in primes4digits and 8147 in get_permutations(1487)

    for p in primes4digits:
        if p != 1487:
            permutations = list(filter(lambda x: x > p and x in primes4digits,
                                       get_permutations(p)))
            for p2 in permutations:
                p3 = p2 + (p2 - p)
                if p3 in permutations:
                    return ''.join([str(x) for x in [p, p2, p3]])
    return 'Not found'

if __name__ == '__main__':
    print(main())
