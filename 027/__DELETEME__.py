#!/usr/bin/python

import math

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
            
def esPrimo (n, primos):
    if len(primos)<=0 or n>primos [-1]:
        calcularPrimos (primos, n)
    if n in primos:
        return True
    else:
        return False

def firstNonPrime (a, b, primos):
    
    n=1L
    parar=False
    while parar==False:
        sum=n**2+a*n+b
        if esPrimo (sum, primos):
            n+=1
        else:
            parar=True
    return n

####################################################################################################
################# Función principal ################################################################
####################################################################################################
def menos (x):
    return -x

primos = []
calcularPrimos (primos, 999)
aes=range (-999, 999, 1)
bes=primos+map (menos, primos)

bestA=0;
bestB=0;
bestLong=0;
for a in aes:
    for b in bes:
        size= firstNonPrime (a, b, primos)
        if size>bestLong:
            bestLong=size
            bestA=a
            bestB=b
print bestA*bestB
