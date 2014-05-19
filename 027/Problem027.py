
import sys
sys.path.insert(0, '../Common/py/')
from Problem import Problem
from Util import Util

class Problem027(Problem):
	""" Euler problem number 27 """

	PN	=	27;
	PT	=	"Quadratic primes";
	PD	=	"Euler discovered the remarkable quadratic formula:\n" + \
			"\n" + \
			"n² + n + 41\n" + \
			"\n" + \
			"It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.\n" + \
			"\n" + \
			"The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.\n" + \
			"\n" + \
			"Considering quadratics of the form:\n" + \
			"\n" + \
			"n² + an + b, where |a| < 1000 and |b| < 1000\n" + \
			"\n" + \
			"where |n| is the modulus/absolute value of n\n" + \
			"e.g. |11| = 11 and |−4| = 4\n" + \
			"\n" + \
			"Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.\n"
	PDT	=	1000;

	def __init__(self, args):
		""" Default constructor. """
		Problem.__init__(self, self.PN, self.PT, self.PD, self.PDT, args)

	def solve (self, n):
		""" Solves the euler problem 027 """
		util = Util();
		util.calcPrimes(n-1)
		aes = range(-(n-1), n-1, 1)
		bes = util.primes + map(lambda x: -x, util.primes)

		bestA=0
		bestB=0;
		bestLong=0;
		for a in aes:
			for b in bes:
				size = util.firstNonPrime (a, b, primes)
				if size>bestLong:
					bestLong=size
					bestA=a
					bestB=b
		return bestA*bestB
