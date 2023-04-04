# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:39:40 2023

@author: Usuario
"""

lista_flujos=[100,200,300,400,500]
tir=0.2
def valor_actual(tir,lista_flujos):
    if len(lista_flujos)==0:
        return 0
    else:
        elemento_a_modificar=lista_flujos[-1]
        numero_de_periodos=len(lista_flujos)
    elemento_a_modificar=elemento_a_modificar/((1+tir)**(numero_de_periodos-1))
    lista_flujos=lista_flujos[:-1]
    return elemento_a_modificar+valor_actual(tir, lista_flujos)
resultado=(valor_actual(tir, lista_flujos))
resultado_redondeado=round(resultado,2)
print(resultado_redondeado)