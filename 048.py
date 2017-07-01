"""
Project Euler Problem 48
========================

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

from functools import reduce


def get_last_digits_until(until, num_digits=10):
    '''
    Returns the num_digits last digits of the series
    1^1 + 2^2 + 3^3 + ... + until^until
    '''
    maxint = 10**num_digits

    def add(x, y): return (x + y) % maxint
    def multiply(x, y): return (x * y) % maxint
    def pow(b, e): return reduce(multiply, [b]*e)
    def sum(l): return reduce(add, l)

    # Literally, 1^1 + 2^2 + 3^3 + ... + until^until
    return sum([pow(x, x) for x in range(1, until+1)])


def main():
    assert get_last_digits_until(10) == 405071317
    assert get_last_digits_until(10, 12) == 10405071317
    return get_last_digits_until(1000)

if __name__ == "__main__":
    print(main())
