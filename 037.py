"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from util import PrimeFactory


def find_truncable_primes(n):
    """
    The numbers will start with [2, 3, 5, 7] and end with [3, 7] (if it ended in
    2 or 5 it would be multilpe of 2 or 5).

    We can build backwards:
        - primes that end in [3, 7]: [13, 17, 23, 37, 43, 47, 53, 67, 73, 83,
        97]
        - primes that start with [2, 3, 5, 7]: [23, 29, 31, 37, 53, 59, 71, 73,
        79]
        - s would be [23, 37, 53, 73]
        - primes that end in [13, 17, 23, 37, 43, 47, 53, 67, 73, 83, 97]: [233]
    """
    s = []
    prime_factory = PrimeFactory()
    r = [7, 3]  # Right, endings
    l = [2, 3, 5, 7]  # Left, starters

    n = 2
    while True:
        prime_factory._calc_primes(10**n)
        r = [p for p in prime_factory.primes if (p % 10**(n-1)) in r and
             p < 10**n and p >= 10**(n-1)]
        l = [p for p in prime_factory.primes if (p // 10) in l and
             p < 10**n and p >= 10**(n-1)]
        v = [x for x in r if x in l]
        s += v
        if l == [] or r == []:
            break
        # We are told that there are 11 primes
        if len(s) == 11:
            break
        n += 1
    return s


def solve(n):
    return sum(find_truncable_primes(n))

if __name__ == "__main__":
    print(solve(1000000))
