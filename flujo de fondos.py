# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:28:33 2023

@author: Usuario
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 07:29:56 2023

@author: gbasa
"""

class FF():
    """ Documentacion que va al __doc__ del objeto
        Poner aqui lo que se quiera explicar en un help.
        Por una cuestion de seguridad, vamos a usar tuplas 
        para garantizar la inmutabilidad del objeto
        """
    def __init__(self,tupla=tuple()):
        self.flujos=tupla
        
    def van(self,tasa, n=0):
        """ Calculo de valor actual neto recursivo
            Inputs: 
                1 - tasa (posicional)
                2 - n posicion en el vector ( default = 0, named argument ). 
                    Sirve para manejar recursivamene las iteraciones 
                    sin alterar la lista del flujo de fondos  
        """
        if len(self.flujos)>0:
            if n==len(self.flujos):
                salida = 0
            else:
                salida = self.flujos[n]+1.0/(1.0+tasa)*self.van(tasa, n=n+1)
        else:
            print('\n',"La tupla de flujo de fondos esta vacia. Se devuelve 0")
            salida = 0
        return salida
    
    def vt(self,tasa,t = 0):
        """ Calculo de valor del flujo de fondos a un tiempo t
            Funciona calculando van y luego llevando a tiempo t correspondiente
            Inputs: 
                1 - tasa (posicional)
                2 - t momento de valuacion ( default = 0, named argument ). 
                    
        """
        return self.van(tasa)*(1.0+tasa)**t
    def tir(self,a,b,tol,n):
        paso= round((max(a,b)-min(a,b))/n,4)
        lista_cambios_de_signo=[]
        for elemento in range(n):
            tasa1 = a + elemento*paso
            tasa2=a + (elemento+1)*paso
            van1= self.van(tasa1)
            van2=self.van(tasa2)
            if  round(van1,tol)==0:
                tir=tasa1
                return tir
            elif round(van2,tol)==0:
                tir=tasa2
                return tir
            elif( van1>0 and van2<0) or (van1<0 and van2>0):
                lista_cambios_de_signo.append([tasa1,tasa2])
            
            
        return self.tir(lista_cambios_de_signo[-1][0],lista_cambios_de_signo[-1][-1],tol,n)
    def tir_GS(self,a,b,tol):
        tasa=self.tir(a, b, tol, 10)
        return tasa
    def tir_BI (self,a,b,tol):
        tasa= self.tir(a, b, tol,2)
        return tasa
    def tir_AS (self,tol,a=0,h=0.05):

        vanA= self.van(a)
        vanH=self.van(a+h)
        if  round(vanA,tol)==0:
            salida=a
        elif (vanA>0 and vanH<0) or (vanA<0 and vanH>0):
            salida=round(self.tir(a,round(a+h,4),tol,2),4)
            
        else:
            if vanA>vanH:
                a=a+h
            else:
                a=a-h
            
            salida= self.tir_AS(tol,a,h)
        return salida
#%%
if __name__=='__main__':
    
    c = FF((-80,10,10,10,10,10,10,10,10,100))    
    # dos formas de llamar al help    
    # print((c.van).__doc__)
    # help(c.vt)        
        
    # # Busqueda de TIR...
    # for x in range(1,20) : print(x, c.van(x/100.0))   
    
    # # van a un valor proximo a la tir...
    # print('\n',c.van(0.1330055))
    
    # Valor futuro en t a la tir. 
    # Notar que al no ser la tir exacta, 
    # a 25 periodos hacia el futuro, se aleja del 0.
    # Haria falta una funcion para computar la tir.... :) 
    # print('\n', c.vt(0.1330055,25))
    print(c.tir_GS(0, 1,2))
    print(c.tir_BI(0, 1, 2))
    print(c.tir_AS(2))
    
    #test caso FF vacio
    # a = FF()
    # print('\n',a.van(0.0))