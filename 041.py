"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# THOUGHTS:
#
# There is no 9-digit pandigital prime, because 1+2+3+..+9 = 45 and 45%3 = 0,
# so all the 9-digit pandigitals are also divisible by 3
# 1+2+..+8 = 36 and 36 % 3 = 0
# 1+2+..+7

from itertools import permutations
from util import PrimeFactory


def main():
    factory = PrimeFactory()
    for num_digits in range(7, 1, -1):
        for num_list in permutations(range(num_digits, 0, -1)):
            num = int(''.join(map(str, num_list)))
            if factory.is_prime(num):
                return num
    return 'No pandigital prime found??'


if __name__ == "__main__":
    print(main())
