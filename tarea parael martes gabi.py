# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:53:19 2023

@author: Usuario
"""

def primos(n):
    lista_descomposicion=[1]    
    while n!=1:
        for numero in range(2,n+1):
            if n%numero==0:
                n=n//numero
                lista_descomposicion.append(numero)
                break
    return lista_descomposicion
def factores_primos(a,b):
    lista_a=primos(a)
    lista_b=primos(b)
    lista_combinados=[]
    for numero in lista_a:
        if numero in lista_b:
            lista_combinados.append(numero)
            lista_b.remove(numero)
    MCD=1
    for numero in lista_combinados:
        MCD=MCD*numero
    return MCD
a=int(input("Eliga el numero a: "))
b=int(input("Eliga el numero b: "))
MCD=factores_primos(a, b)
print(MCD)