#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
""" \brief Calcula tantos primos como se indique y los guarda en un
vector
\param primos Un vector de primos
\param hasta El mayor número que queremos comprobar si es primo. Si
hasta es primo, se añadirá al vector
"""
def calcularPrimos (primos, hasta):
    cambia=False
    i=0L

    if len(primos)==0:
        primos.append (2L)
        cambia=True
        i=3L
    else:
        i=primos [-1]+2L
    while i<=hasta:
        esPrimo=True
        raiz=math.sqrt(i)//1
        for iter in primos:
            if iter > raiz:
                break;
            elif i%iter==0:
                    esPrimo=False
        if esPrimo:
            primos.append (i)
            cambia=True
        i+=2
    return cambia

####################################################################################################
"""
\brief Calcula los divisores primos de un número. Hace uso de calcularPrimos
\param n El número base
\param primos Una lista de primos, posiblemente incompleta
"""
def divisoresPrimos (n, primos):
    divisores=[]
    cambia=True
    while cambia and n!=1:
        for iter in primos:
            if n==1:
                break
            while n%iter==0:
                divisores.append (iter)
                n/=iter
        cambia=calcularPrimos (primos, n)
    return divisores

####################################################################################################
"""
\brief Calcula los divisores primos de un número. Hace uso de calcularPrimos
\param n El número base
\param primos Una lista de primos, posiblemente incompleta
"""
def descomposicion (n, primos):
    divisores=[]
    cambia=True
    while cambia and n!=1:
        for iter in primos:
            if n==1:
                break
            numNs=0;
            while n%iter==0:
                numNs+=1
                n/=iter
            if numNs>0:
                divisores.append ((iter,numNs))
        cambia=calcularPrimos (primos, n*2)
    return divisores

####################################################################################################
"""
\brief Indica si dos números son iguales (listas)
"""
def iguales (listaA, listaB):
    sonIguales=True
    if len (listaA) != len (listaB):
        sonIguales=False
    else:
        for a in listaA:
            if not a in listaB:
                sonIguales=False
                break;
    return sonIguales

####################################################################################################
"""
\brief Eleva un número a una potencia
"""
def elevar (lis, e):
    nuevaLista=[]
    for l in lis:
        tup=(l[0],l[1]*e)
        nuevaLista.append (tup);
    return nuevaLista

####################################################################################################

def findMaxCommDiv (num, den): 
	"reducir la fracción:"
	divisores = range(num, 1, -1)
	for divisor in divisores:
		if num%divisor==0 and den%divisor==0:
			return divisor;
	return 1;

####################################################################################################

def numCircularPrimes (digits, num, totalDigits, primes):
	if digits!=0 :
		sum = 0
		for digit in range (1, 10, 2) :
			sum += numCircularPrimes (digits-1, num*10 + digit, totalDigits+1, primes)
		return sum
	else :
		isCircular = True
		for rot in range (0, totalDigits):
			if not num in primes:
				isCircular = False
			else:
				num = num/10 + (num%10)*(10**(totalDigits-1))
		if isCircular:
			return totalDigits
		else:
			return 0

####################################################################################################

def getNumDigits(num):
	nDigits=0 
	nCpy = num 
	while (nCpy != 0):
		nDigits+=1
		if num!=2 and (nCpy%10)%2 == 0:
			return 0
		nCpy = nCpy//10
	return nDigits

####################################################################################################

def getCircularNumbers(num, nDigits): 
	circularNumbers=[]
	ex = 10**(nDigits-1)
	for rot in range (0, nDigits):
		circularNumbers.append(num)
		num = num/10 + (num%10)*ex
	return circularNumbers
	
####################################################################################################

numsToCheck = range (2, 1000000)
primes=[]
calcularPrimos(primes, 1000000)

# Find all the primes below one million
# isCircPrime=0 (not c.prime), =1 (is c.prime) =2 (could be) "
isCircPrime = [0] * 1000001
maxPrime=0
for prime in primes:
	isCircPrime[prime] = 2
	maxPrime=prime

#for i in range (2, maxPrime+1):
for i in primes:
	if isCircPrime[i] == 2 :
		numDig = getNumDigits(i)
		isCircular=True
		if numDig<=0:
			isCircular=False
			isCircPrime [i] = 0
		else:
			circNumbers = getCircularNumbers(i, numDig) 
			for n in circNumbers:
				if not n in primes:
					isCircular=False
			for n in circNumbers:
				isCircPrime [n] = 1 if isCircular else 0

print "Solution " , isCircPrime.count(1)

#solution=0
#for digits in range (1, 10) :
#	solution += numCircularPrimes(digits, 0, 0, primes)
#print "The solution is " + solution



