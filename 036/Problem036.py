
import sys
sys.path.insert(0, '../Common/py/')
from Problem import Problem

#####################################################################################################
#										THOUGHTS:													#
# 																									#
# We are only interested in odd numbers (if have to start with 1, has to end with 1).				#
# Instead of check every number until one million if they are palindromic in both bases,			#
# create palindromic numbers in one base and check in the other.									#
# Maybe it's easier to build the number in base 10 and check in base 2.								#
#####################################################################################################

class Problem036(Problem):
	""" Euler problem number 36 """

	PN	=	36;
	PT	=	"Double-base palindromes";
	PD	=	"The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.\n" + \
			"Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.\n" + \
			"(Please note that the palindromic number, in either base, may not include leading zeros.)\n";
	PDT	=	1000000;

	def __init__(self, args):
		""" Default constructor. """
		Problem.__init__(self, self.PN, self.PT, self.PD, self.PDT, args)

	def solve (n):
		""" Solves the euler problem 036 """
		return 123;
