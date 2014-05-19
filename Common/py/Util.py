
import math

class Util:
	""" A common set of methods to help solve all the euler problems """

	# TODO: Store things like lists of primes


	######################################################################

	def getDigits(self, num, base):
		""" Returns a list of int with all the digits of a number (using an arbitrary base) """
		digits = []
		while num > 0:
			dig = num%base
			digits.append(dig)
			num = num//base
		return digits

	######################################################################

	def getNumDigits(self, num, base):
		""" Returns the number of digits of a number, i.e. int(log(num, base)) """
		cnt = 0
		while num>0:
			cnt += 1
			num //= base
		return cnt

	######################################################################

	def isPalindromic (self, num, base):
		""" Check if a number is palindromic in a base (the number has no leading zeros) """
		digits = Util.getDigits(num, base)
		pal = True
		for d in reversed(digits):
			lastDig = num%base
			if d != lastDig:
				pal = False
				break
			num//=base

		return pal

	######################################################################

	def periodSize (self, denominator):
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

	######################################################################

	primes = []

	def calcPrimes (self, til):
		""" Calc and store a list with primes until the number "til" """
		change = False
		i = 0

		if len(self.primes) == 0:
			self.primes.append (2)
			change = True
			i = 3
		else:
			i = self.primes [-1]+2
		while i <= til:
			isPrime = True
			root = math.sqrt(i)//1
			for iter in self.primes:
				if iter > root:
					break
				elif i % iter == 0:
					isPrime=False
			if isPrime:
				self.primes.append (i)
				change=True
			i+=2
		return change

	######################################################################

	def primeDivisors (self, n):
		divisors=[]
		change=True
		while change and n!=1:
			for iter in self.primes:
				if n==1:
					break
				while n%iter==0:
					divisors.append(iter)
					n/=iter
				cambia=calcPrimes(self.primos, n)
		return divisors

	######################################################################

	def isPrime (self, n):
		if len(self.primes)<=0 or n>self.primes [-1]:
			calcPrimes (self.primes, n)
		if n in self.primes:
			return True
		else:
			return False

	######################################################################

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

	######################################################################

