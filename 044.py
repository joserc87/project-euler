"""
Project Euler Problem 44
========================

Pentagonal numbers are generated by the formula, P[n]=n(3n-1)/2. The first
ten pentagonal numbers are:

               1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P[4] + P[7] = 22 + 70 = 92 = P[8]. However, their
difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P[j] and P[k], for which their sum
and difference is pentagonal and D = |P[k] - P[j]| is minimised; what is
the value of D?
"""


class PentagonalHelper:
    """
    Helper class to calculate the pentagonal numbers. We can use the brackets
    operator (P[X]) as well as the contains operator (X in P).
    """
    def __init__(self):
        # P[0] == 0 to make our lifes easier, as pentagonals start from 1
        self.pentagonals = [0]

    def P(self, n):
        """Returns the n-th pentagonal number (n>=1)"""
        return (n*(3*n-1))//2

    def _build(self, last):
        next_item = len(self.pentagonals)
        self.pentagonals += [self.P(n) for n in range(next_item, last+1)]

    def _build_until_pentagonal(self, last_p):
        next_item = len(self.pentagonals)
        while self.pentagonals[-1] < last_p:
            self.pentagonals.append(self.P(next_item))
            next_item += 1

    def __contains__(self, p):
        self._build_until_pentagonal(p)
        return p in self.pentagonals

    def __getitem__(self, n):
        if n >= len(self.pentagonals):
            self._build(n)
        return self.pentagonals[n]


# Test
P = PentagonalHelper()
assert [P[i] for i in range(1, 11)] == [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
assert 117 in P
assert 118 not in P

################
# One solution #
################

# THOUGHTS:
#
# The series grows exponentially. That means that, if we find an n and a k so
# that P[n] + P[n+k] in P and D = P[n+k] - P[n] in P, we only have to look until
# the point of m where P[m+1] - P[m] > D. At that point in the series, it is
# impossible to find a lower D.
#
# WARNING:
# This solution is very fast in finding a solution to the problem, but it does
# not assure that the first solution is the one with the minium value of D!


def S_tuple(pair):
    return P[pair[1]] + P[pair[0]]


def D_tuple(pair):
    return P[pair[1]] - P[pair[0]]


def find_second_pair(n, min_pair_found):
    """Finds a second pair of pentagonal m, m<n so that P[m] + P[n] in P and
    P[n] - P[m] in P"""
    for m in range(n-1, 0, -1):
        pair = m, n
        if min_pair_found and D_tuple(pair) > D_tuple(min_pair_found):
            return None
        if S_tuple(pair) in P and D_tuple(pair) in P:
            return pair
    else:
        return None


def main_1():
    n = 2
    min_pair = None
    while True:
        if min_pair is not None and D_tuple((n, n+1)) > D_tuple(min_pair):
            break
        pair = find_second_pair(n, min_pair)
        if pair is not None and (min_pair is None or D_tuple(pair) <
                                 D_tuple(min_pair)):
            min_pair = pair
            # Comment this break to find any other possible (better) solution
            break
        n += 1
    return D_tuple(min_pair)

####################
# Another solution #
####################

# We want to minimise D = P[n+k] - P[n]. So we can check the possible solutions
# in order of D value. If the numbers are:

# We can have an array with tuples (D, k), initialized to (0, 0). Then we
# iterate over that array over and over for different values of D. If the
# pentagonal numbers are:
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145

# Then we would do:
# None
# D=1: None, (1, 4)
# D=5: None, None, (1, 7)
# D=9: None, None, (2, 11), (1, 10)
# D=11: None, None, (2, 11), (2, 17), (1, 12)
# D=12: None, None, None, (2, 17), (1, 12)
# D=13: None, None, None, (2, 17), (2, 23), (1, 16)
# D=17: None, None, None, (2, 17), (2, 23), (2, 29), (1, 19)
#
# NOTE: The last tuple should always be t[0] == 1
# NOTE: We can also skip some Ds of course!
#
# Algo:
# D=4, L=[None, (1,4)]
# While not found:
#   Go through the list and find the items i with i.D==D
#   Update i.k++ and calculate their new i.D, or set it to null if k >= i
#   if the last L[-1].k > 1, add a new element
#   Check if some of the updated elements passes the condition. If so, return
#   the lowest one
#   D = min(i.D) + 1
#
# NOTE: the first element found has the lowest D!
#
# WARNING:
# This method should retrieve the correct solution, but it has not been tested
# as it takes too much time to complete.


def S(el):
    return P[el.idx - el.k] + P[el.idx]


def D(el):
    '''Returns -1 if el.idx - el.k <= 0'''
    return -1 if el.idx - el.k <= 0 else P[el.idx - el.k] - P[el.idx]


class Element:
    def __init__(self, idx, k=1, d=None):
        self.idx = idx
        self.k = k
        self.d = d


def main_2():
    # We will iterate over the value of d to get the pentagonal with the minimum
    # d
    d = 1
    # A helper list to iterate over the pair of pentagonals in order of D. Each
    # item will be a pair (k, d), where k the fines the pair (P[i-k], P[i]) and
    # d is the D value of that pair (d=P[i-k] - P[i]).
    l = [None]
    iteration = 0
    while True:
        solutions = []
        # Go throught the list and find the items i with i.D = D
        updated_elements = []
        for element in l:
            if element is not None and element.d == d:
                # Update i.k++ and calculate their new i.D, or set it to null if
                # k >= i
                element.k += 1
                element.d = D_tuple(element)
                updated_elements.append(element)
        # Check if some elements have to be set to None
        for element in updated_elements:
            if element.d < 0:
                l[element.idx] = None

        # If the last element has k > 1, we need to add a new element
        if l[-1] is None or l[-1].k > 1:
            el = Element(idx=len(l), k=1)
            el.d = D_tuple(el)
            l.append(el)
            updated_elements.append(el)

        # Check if we found a solution
        solutions = [uel for uel in updated_elements if uel.d > 0 and
                     D_tuple(uel) in P and S_tuple(uel) in P]
        if solutions != []:
            optimal_solution = min(solutions, key=lambda x: x.d)
            return optimal_solution.d

        # Update d to search for the next element
        d = min([x for x in l if x is not None], key=lambda x: x.d).d
        iteration += 1

if __name__ == '__main__':
    print(main_1())