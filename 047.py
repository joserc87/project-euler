"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

from collections import deque
from util import PrimeFactory


def distinctive_factors(factors):
    for i, factors1 in enumerate(factors):
        for factors2 in [f for j, f in enumerate(factors) if j > i]:
            for f in factors1:
                if f in factors2:
                    return False
    return True


def find_n_cons_nums(n):
    """Finds the first n consecutive numbers that have n disctintive prime
    factors"""

    primes = PrimeFactory()

    # First number that can be decomposed is 4
    i = 4
    factors = deque([primes.get_prime_factors(f) for f in range(i, i+n)])
    while sum([0 if len(f) == n else 1 for f in factors]) != 0 or \
            not distinctive_factors(factors):
        factors.rotate()
        i += 1
        factors[-1] = primes.get_prime_factors(i + n - 1)
    return i


def main():
    assert find_n_cons_nums(2) == 14
    assert find_n_cons_nums(3) == 644
    print(find_n_cons_nums(4))

if __name__ == '__main__':
    main()
