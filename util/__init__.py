
import math


def get_digits(num, base=10):
    """Transforms an int into a list of integers with the digits in an arbitrary
    base"""
    digits = []
    while num > 0:
        digits.append(num % base)
        num = num//base
    return digits[::-1]


def get_int_from_digits(digits, base=10):
    n = 0
    for digit in digits:
        n *= base
        n += digit
    return n


def is_palindromic(num, base=10):
    """Check if a number is palindromic in an arbitrary base (the number has no
    leading zeros)"""
    digits = get_digits(num, base)
    return digits == digits[::-1]


def get_num_digits(num, base=10):
    """Returns the number of digits of a number, i.e. int(log(num, base))"""
    cnt = 0
    while num > 0:
        cnt += 1
        num //= base
    return cnt


def get_rotations(num, base=10):
    """Returns a list with all the rotations of a number, e.g. [123, 312, 231]
    for the number 123"""
    rotations = []
    n = num
    nd = get_num_digits(num, base)
    for i in range(nd):
        rotations.append(n)
        d = n % base
        n = (n // base) + (base**(nd-1))*d
    return rotations


def period_size (self, denominator):
    """ This functions finds the size of the period
        given a fraction 1/denominator """
    size = 0
    # numerador, denominador y resto
    numerator = 1
    step = (numerator,0)
    stepList = []
    stop = False
    # Loop, while cant find the period
    while stop == False:
        div = numerator // denominator
        minder = numerator % denominator
        currentStep = (numerator, minder)
        numerator = minder*10
        if currentStep in stepList:
            stop = True
            stepList.reverse ()
            size = stepList.index (currentStep)+1
        else:
            stepList.append (currentStep)
            if minder == 0:
                stop = True
                size = 0
    return size


class PrimeFactory:

    def __init__(self):
        self.primes = [2, 3]
        self.last_number_checked = 3

    def _calc_primes(self, until):
        """ Calc and store a list with primes until the number "until" """
        # If only odd numbers will be prime, so if an even number is given,
        # check one extra number
        if until % 2 == 0:
            until += 1

        change = False
        if until > self.last_number_checked:
            i = self.last_number_checked + 2
            while i <= until:
                isPrime = True
                root = math.sqrt(i)//1
                for iter in self.primes:
                    if iter > root:
                        break
                    elif i % iter == 0:
                        isPrime = False
                if isPrime:
                    self.primes.append(i)
                    change = True
                i += 2

            self.last_number_checked = until
        return change

    def is_prime(self, n):
        self._calc_primes(n)
        return n in self.primes

    def __contains__(self, n):
        return self.is_prime(n)

    def firstNonPrime (self, a, b):
        n = 1
        stop = False
        while stop == False:
            sum = n ** 2 + a * n + b
            if isPrime (sum):
                n += 1
            else:
                stop = True
        return n

    def get_prime_factors(self, n):
        factors = []
        i = 0
        self._calc_primes(n)
        for prime in self.primes:
            if n == 1:
                break
            times = 0
            while n % prime == 0:
                n /= prime
                times += 1
            if times > 0:
                factors.append((prime, times))
        return factors
