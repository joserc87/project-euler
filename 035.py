"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from util import get_rotations, PrimeFactory


def get_circular_primes_dummy(n):
    # Dummy
    circular_primes = []
    prime_factory = PrimeFactory()
    for i in range(1, n+1):
        rotations = get_rotations(i)
        if len([x for x in rotations if prime_factory.is_prime(x)]) == \
                len(rotations):
            circular_primes.append(i)
    return circular_primes


def get_circular_primes(n):
    prime_factory = PrimeFactory()
    prime_factory._calc_primes(n)

    # is_circular_prime[i] contains:
    # * 0 if i is not a circular prime
    # * 1 if i is a circular prime
    # * 2 if i _could be_ a circular prime
    is_circular_prime = [0] * (n+1)
    primes = [p for p in prime_factory.primes if p < n]
    for prime in primes:
        is_circular_prime[prime] = 2

    for i in primes:
        if is_circular_prime[i] == 2:
            rotations = get_rotations(i)
            are_primes = True
            for rotation in rotations:
                if not prime_factory.is_prime(rotation):
                    are_primes = False
                    break
            # If it's not a circular prime, neither is its rotations
            # Note:
            # We need to be careful with numbers ending or containing a 0. For
            # example, 11 is a circular prime, but 101 is not, although 011 is a
            # rotation of 101
            for rotation in rotations:
                if is_circular_prime[rotation] == 2:
                    is_circular_prime[rotation] = 1 if are_primes else 0

    assert is_circular_prime.count(2) == 0
    circular_primes = [i for i in range(n) if is_circular_prime[i] == 1]
    return circular_primes


def solve(n):
    return len(get_circular_primes(n))

if __name__ == "__main__":
    # Test
    print(solve(1000000))
