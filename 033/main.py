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

"""
\brief Comprueba que dos numeros comparten al menos un dígito común
\param a El primer número, entre 10 y 98
\param b El segundo número, entre a+1 y 99
"""
def isCurious (a, b):
	a1 = a//10
	a2 = a%10
	b1 = b//10
	b2 = b%10 
	return (a2 != 0 or b2 != 0) and ((a1 == b1 and (1.0*b2*a)/b == a2) or \
		(a1 == b2 and (1.0*b1*a)/b == a2) or \
		(a2 == b1 and (1.0*b2*a)/b == a1) or \
		(a2 == b2 and (1.0*b1*a)/b == a1)); 

prodNumerador = 1
prodDenominador = 1
numeradores = range (11, 99)
for numerador in numeradores:
    denominadores = range (numerador+1, 100)
    for denominador in denominadores:
	    if (isCurious(numerador, denominador)):
		    print 'La fraccion ' + repr(numerador) + '/' + repr(denominador) + ' es curiosa'
		    prodNumerador *= numerador
		    prodDenominador *= denominador 
		    divisor = findMaxCommDiv(prodNumerador, prodDenominador)
		    prodNumerador /= divisor
		    prodDenominador /= divisor; 

"reducir la fracción:"
print 'La solucion es ' + repr(prodDenominador)


