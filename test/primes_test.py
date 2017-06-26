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

    def test_contains(self):
        primes = PrimeFactory()
        self.assertTrue(2 in primes)
        self.assertTrue(3 in primes)
        self.assertTrue(5 in primes)
        self.assertTrue(7 in primes)
        self.assertTrue(11 in primes)
        self.assertTrue(13 in primes)
        self.assertTrue(17 in primes)

    def test_get_prime_factors(self):
        primes = PrimeFactory()
        self.assertEquals([(2, 2), (7, 1), (23, 1)],
                          primes.get_prime_factors(644))
        self.assertEquals([(3, 1), (5, 1), (43, 1)],
                          primes.get_prime_factors(645))
        self.assertEquals([(2, 1), (17, 1), (19, 1)],
                          primes.get_prime_factors(646))


if __name__ == '__main__':
    unittest.main()
