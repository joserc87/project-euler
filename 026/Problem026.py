
import sys
sys.path.insert(0, '../Common/py/')
from Problem import Problem
from Util import Util

class Problem026(Problem):
	""" Euler problem number 26 """

	PN	=	26
	PT	=	"Double-base palindromes"
	PD	=	"A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:\n" + \
			"\t1/2	= 	0.5\n" + \
			"\t1/3	= 	0.(3)\n" + \
			"\t1/4	= 	0.25\n" + \
			"\t1/5	= 	0.2\n" + \
			"\t1/6	= 	0.1(6)\n" + \
			"\t1/7	= 	0.(142857)\n" + \
			"\t1/8	= 	0.125\n" + \
			"\t1/9	= 	0.(1)\n" + \
			"\t1/10	= 	0.1\n" + \
			"Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.\n" + \
			"\n" + \
			"Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.\n"
	PDT	=	1000

	def __init__(self, args):
		""" Default constructor. """
		Problem.__init__(self, self.PN, self.PT, self.PD, self.PDT, args)

	def solve (self, n):
		""" Solves the euler problem 026 """
		util = Util()
		denominator = 2
		maxCycle = 0
		d = 2
		bestD = 0
		while d<n:
			cycle = util.periodSize(d)
			if cycle > maxCycle:
				maxCycle=cycle
				bestD=d
			d+=1
		return bestD

