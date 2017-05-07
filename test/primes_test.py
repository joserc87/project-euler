import unittest
from util import PrimeFactory


class TestPrimeFactory(unittest.TestCase):

    def test_calc_primes(self):
        sut = PrimeFactory()
        sut._calc_primes(20)
        self.assertEqual(sut.last_number_checked, 21)
        self.assertEqual(sut.primes, [2, 3, 5, 7, 11, 13, 17, 19])

    def test_is_prime(self):
        primes = PrimeFactory()
        self.assertTrue(primes.is_prime(2))
        self.assertTrue(primes.is_prime(3))
        self.assertTrue(primes.is_prime(5))
        self.assertTrue(primes.is_prime(7))
        self.assertTrue(primes.is_prime(11))
        self.assertTrue(primes.is_prime(13))
        self.assertTrue(primes.is_prime(17))

if __name__ == '__main__':
    unittest.main()
