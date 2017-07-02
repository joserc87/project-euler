"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from itertools import islice
from util import PrimeFactory

# Yes, this is a global variable. YOLO!
primes = PrimeFactory()


def get_prime_with_longest_sequence_under(top):
    # Calculate the hypothetical longest chain (2+3+5...)
    primes._calc_primes(top)
    theorical_maximum = 0
    target = top
    for p in primes.primes:
        target -= p
        theorical_maximum += 1
        if target <= 0:
            break

    for n in range(theorical_maximum, 1, -1):
        # Check if there is a chain that long
        for start in range(0, len(primes.primes)-n):
            s = sum(islice(primes.primes, start, start+n))
            if s > top:
                break
            elif s in primes:
                return s


def main():
    assert get_prime_with_longest_sequence_under(100) == 41
    assert get_prime_with_longest_sequence_under(1000) == 953
    return get_prime_with_longest_sequence_under(1000000)

if __name__ == '__main__':
    print(main())
