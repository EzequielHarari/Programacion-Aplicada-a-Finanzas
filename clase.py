# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:31:55 2023

@author: Usuario
"""

class ff:
    def __init__(self,flujos,tasa):
        self.flujos=flujos
        self.tasa=tasa
    def valor_actual(self, tir,n=0):
        self.tasa=tir
        if n==len(self.flujos):
            salida= 0
        else:
            salida=self.flujos[n]+1/(1+tir)*self.valor_actual(tir,n+1)
            
        salida= self.valor_actual(tir, self.flujos)
        return salida
    
    