"""
Project Euler Problem 43
========================

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1st digit, d[2] be the 2nd digit, and so on. In this
way, we note the following:

  * d[2]d[3]d[4]=406 is divisible by 2
  * d[3]d[4]d[5]=063 is divisible by 3
  * d[4]d[5]d[6]=635 is divisible by 5
  * d[5]d[6]d[7]=357 is divisible by 7
  * d[6]d[7]d[8]=572 is divisible by 11
  * d[7]d[8]d[9]=728 is divisible by 13
  * d[8]d[9]d[10]=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

# THOUGHTS:
#
# I could handcraft those pandigitals, making them already sub-string divisible
# by 2, 3, etc. In the other hand...
#
# YOLO! BRUTE FORCE FTW!

from itertools import permutations


def l2int(permutation):
    """Transform a permutation(list of num) ton int"""
    return int(''.join(map(str, permutation)))


def check_substr_divisibility(p):
    return l2int(p[1:4])  % 2  == 0 and \
           l2int(p[2:5])  % 3  == 0 and \
           l2int(p[3:6])  % 5  == 0 and \
           l2int(p[4:7])  % 7  == 0 and \
           l2int(p[5:8])  % 11 == 0 and \
           l2int(p[6:9])  % 13 == 0 and \
           l2int(p[7:10]) % 17 == 0

assert check_substr_divisibility('1406357289')


def main():
    pandigitals = permutations(range(10))
    filtered = [l2int(p) for p in pandigitals if check_substr_divisibility(p)]
    return sum(filtered)

if __name__ == "__main__":
    print(main())
