#!/usr/bin/python

def posibilidades (tiposMonedas, cantidad, under=200):
    if cantidad==0:
        return 1
    elif cantidad==1:
        return 1
    numPosibilidades=0
    for m in tiposMonedas:
        if m <= cantidad and m <= under:
            numPosibilidades+=posibilidades (tiposMonedas, cantidad-m, m)
    return numPosibilidades

numPosibilidades=posibilidades ([200, 100, 50, 20, 10, 5, 2, 1], 200)
print numPosibilidades
