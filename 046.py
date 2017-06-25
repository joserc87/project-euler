"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""


# THOUGHTS:
#
# Iterate over all the odd numbers n
# Check that n is not prime
# For every square s, s<n:
#   Check that n - 2*s is not prime

from util import PrimeFactory

primes = PrimeFactory()

# Array with the squares, for efficiency
squares = [0]


def get_squares_until(n):
    i = len(squares)
    while squares[-1] < n:
        squares.append(i*i)
        i += 1
    return [s for s in squares if s < n]


def find_goldbach(n):
    '''Finds the prime p and the square s so that n == p + 2*s'''
    for square in get_squares_until(n):
        p = (n - square*2)
        if p in primes:
            return (p, square)
    # Goldbach conjeture is false!
    return None


def main():
    n = 9
    while True:
        if n not in primes:
            if find_goldbach(n) is None:
                return n
        n += 2

if __name__ == '__main__':
    print(main())
