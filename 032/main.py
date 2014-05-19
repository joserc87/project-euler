#!/usr/bin/python
import math
def getDigitos (n):
    digitos=[]
    while n>0:
        digitos.append (n%10)
        n/=10
    return digitos

def getNumDigitos (n):
    cnt=0
    while n>0:
        cnt+=1
        n/=10
    return cnt

def todos (digitos):
    if len (digitos)!=9:
        return False
    estanTodos=True
    for i in range(1,10):
        if not i in digitos:
            estanTodos=False
    return estanTodos

def pandigital (a, b):
    c = a*b
    digiA = getDigitos (a)
    digiB = getDigitos (b)
    digiC = getDigitos (c)
    digitos = digiA+digiB+digiC
    if todos (digitos):
        return True
    else:
        return False

def digitosRepetidos (n):
    repe=False
    digitos = getDigitos (n)
    if len (digitos)>9:
        return True
    cjto = set(digitos)
    if len (cjto)==len (digitos):
        return False
    else:
        return True
        

#main
a=1
b=1
aMax= 99999 #como mucho, a puede tener 5 dígitos, pues a*b va a tener >= 5
panDigs=[]
while a<aMax:
    b=1
    nDigA = getNumDigitos (a)
    if not digitosRepetidos (a):
        while nDigA+getNumDigitos(b)+getNumDigitos(a*b)<=9:
            if (not a*b in panDigs) and (pandigital (a, b)):
                panDigs.append (a*b)
            b+=1
    a+=1

suma=0
for p in panDigs:
    suma += p
print suma
