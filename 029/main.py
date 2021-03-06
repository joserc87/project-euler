#!/usr/bin/python

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

primos =[]
tamA=100
tamB=100


la=range (2,tamA+1)
lb=range (2,tamB+1)
combinaciones =[]
for a in la:
    aDesc=descomposicion (a, primos)
    for b in lb:
        ab = elevar (aDesc, b)
        if not ab in combinaciones:
            combinaciones.append (ab)
print len(combinaciones)

