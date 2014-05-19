#!/usr/bin/python
hola = "hola"

def tamPeriodo (denominador):
    """Esta función calcula el tamaño del periodo de
    la fracción 1/denominador"""
    tam=0
    """numerador, denominador y resto"""
    numerador=1;
    paso=(numerador,0)
    listaPasos=[]
    parar=False
    # Bucle, mientras que no encontremos un periodo
    while parar==False:
        cociente = numerador//denominador
        resto = numerador % denominador;
        pasoActual=(numerador, resto)
        numerador=resto*10;
        if pasoActual in listaPasos:
            parar=True
            listaPasos.reverse ()
            tam=listaPasos.index (pasoActual)+1
        else:
            listaPasos.append (pasoActual)
            if  resto==0:
                parar=True
                tam=0
    return tam

""" FUNCION PRINCIPAL"""

denominador=2
maximoCiclo=0
d=2
mejorD=0
while d<1000:
    ciclo=tamPeriodo(d)
    if ciclo > maximoCiclo:
        maximoCiclo=ciclo
        mejorD=d
    d+=1
print mejorD




