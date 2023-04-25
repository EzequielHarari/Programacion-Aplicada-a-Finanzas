# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 16:34:12 2023

@author: Usuario
"""
import matplotlib.pyplot as plt
import math
import numpy as np
class polinomio:
    def __init__(self,n=0,coefs=[0]):
        if n+1!= len(coefs):
            raise ValueError("La potencia no coincide con la cantidad de elementos")
        self.n=n
        self.coefs=coefs
        
    def get_expression (self):
        for potencia, elemento in enumerate(self.coefs):
            if elemento< abs(math.exp(-5)):
                elemento=0
            if potencia!=0:
                print("+",elemento,"X" "^",potencia,end="")
            else:
                print("p(x)=",elemento,end="")

    def poly_plt (self,a,b,**kwargs):
        x= np.linspace(a, b,1000)
        y=[sum (self.coefs[i] *elemento**i for i in range(len(self.coefs )))for elemento in x]
        color=kwargs.get("color", "red")
        label= kwargs.get("label", "Polinomio")
        xlabel=kwargs.get("xlabel","X")
        ylabel=kwargs.get("ylabel","Y")
        plt.plot(x,y,color=color,label=label)
        plt.axhline(y=0,color="black" )
        plt.axvline(x=0,color="black")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.show()

    def __call__(self,x):
        return sum(self.coefs[i]*x**i for i in range (len(self.coefs)))
    
    def __add__(self, numero):
        coeficientes=self.coefs.copy()

        if isinstance(numero, int) or isinstance(numero, float):
            coefs2= [numero]+[0]* len(coeficientes)

            
        elif isinstance (numero,polinomio):
            coefs2=numero.coefs
            if len(coeficientes)>len(coefs2):
                coefs2+=[0]*(len(coeficientes)-len(coefs2))
            elif len(coefs2)>len(coeficientes):
                coeficientes+=[0]*(len(coefs2)-len(coeficientes))
        else:
            raise ValueError("Lo siento, pero no es posible realizar la suma")
        resultado=[num1+num2 for num1,num2 in zip (coeficientes,coefs2)]
        return self.__class__(len(resultado)-1,resultado)    
    def __radd__(self,numero):
        if isinstance(numero, int) or isinstance(numero, float):
            coeficientes=self.coefs.copy()
            coefs2= [numero]+[0]* len(coeficientes)
            resultado=[num1+num2 for num1,num2 in zip (coeficientes,coefs2)]

            
        else:
            raise ValueError("Lo siento, pero no es posible realizar la suma")
        return self.__class__(len(resultado)-1,resultado)   
    
    def __sub__(self, numero):
        coeficientes=self.coefs.copy()
        
        if isinstance(numero, int) or isinstance(numero, float):
            coefs2= [numero]+[0]* len(coeficientes)
        elif isinstance (numero,polinomio):
            coefs2=numero.coefs
            if len(coeficientes)>len(coefs2):
                coefs2+=[0]*(len(coeficientes)-len(coefs2))
            elif len(coefs2)>len(coeficientes):
                coeficientes+=[0]*(len(coefs2)-len(coeficientes))
        else:
            raise ValueError("Lo siento, pero no es posible realizar la resta")
        resultado=[num1-num2 for num1,num2 in zip (coeficientes,coefs2)]

        return self.__class__(len(resultado)-1,resultado) 
    def __rsub__ (self,numero):
        if isinstance(numero, int) or isinstance(numero, float):
            coeficientes=self.coefs.copy()
            coefs2= [numero]+[0]* len(coeficientes)
        else:
            raise ValueError("Lo siento, pero no es posible realizar la resta")
        resultado=[num1-num2 for num1,num2 in zip (coefs2,coeficientes)]

        return self.__class__(len(resultado)-1,resultado)   
    
    
    def __mul__ (self,escalar):
        coeficientes=self.coefs.copy()
        
        if isinstance(escalar, int) or isinstance(escalar, float):
            coefs2= [escalar]+[0]* self.n
            resultado=[0]*(self.n+len(coefs2))
        elif isinstance (escalar,polinomio):
            coefs2=escalar.coefs
            resultado=[0]*(self.n+ escalar.n+1)
        else:
            raise ValueError("Lo siento, pero no es posible realizar la multiplicacion")
        
        for potencia, numero in enumerate (coefs2):
            for potencia2,numero2 in enumerate (coeficientes):
                elevado= potencia+potencia2
                agregar=numero2*numero
                resultado[elevado]+=agregar
        cantidad=len(resultado)
        for posicion, numero in enumerate(resultado[::-1]):
            if numero==0:
                resultado.pop(cantidad-(posicion+1))
            else:
                break
        return self.__class__(len(resultado)-1,resultado)
    def __rmul__(self,escalar):
        coeficientes=self.coefs.copy()
        
        if isinstance(escalar, int) or isinstance(escalar, float):
            coefs2= [escalar]+[0]* self.n
            resultado=[0]*(self.n+len(coefs2))
        else:
            raise ValueError("Lo siento, pero no es posible realizar la multiplicacion")
        for potencia, numero in enumerate (coefs2):
            for potencia2,numero2 in enumerate (coeficientes):
                elevado= potencia+potencia2
                agregar=numero2*numero
                resultado[elevado]+=agregar
        cantidad=len(resultado)
        for posicion, numero in enumerate(resultado[::-1]):
            if numero==0:
                resultado.pop(cantidad-(posicion+1))
            else:
                break
        return self.__class__(len(resultado)-1,resultado)

    def __floordiv__ (self,numero):
        
        coeficientes= self
        listita=coeficientes.coefs

        if isinstance(numero, int) or isinstance(numero, float):
            coefs2= [numero]
            resultado=[0]*(len(coefs))
        elif isinstance(numero, polinomio):
            coefs2=numero.coefs
            
            resultado=[0]*(len(listita)-len(coefs2)+1)
        else:
            raise ValueError("Lo siento, pero no es posible realizar la division")

        while len(listita)>=len(coefs2):
            diferencia=len(listita)-len(coefs2)
            numero_a_multiplicar= listita[-1]/coefs2[-1]
            resultado[diferencia]=numero_a_multiplicar
            lista=[0]*(diferencia+1)
            lista[-1]=numero_a_multiplicar
            clase=polinomio(len(lista)-1,lista)
            resta=clase*numero
            coeficientes=coeficientes-resta
            listita=coeficientes.coefs
            cantidad=len(listita)
            for posicion, number in enumerate(listita[::-1]):
                if round(number,4)==0.0: 
                    listita.pop(cantidad-(posicion+1))
                else:
                    break
        if len(resultado)==0:
            resultado=[0]
        return self.__class__(len(resultado)-1,resultado)
    def __rfloordiv__(self,numero):
        if isinstance(numero, int) or isinstance(numero, float):
            resultado=[0]
        else:
            raise ValueError("Lo siento, pero no es posible realizar la division")
        return self.__class__(len(resultado)-1,resultado)
                    
    def __mod__(self,numero):
        coeficientes= self
        listita=coeficientes.coefs

        if isinstance(numero, int) or isinstance(numero, float):
            coefs2= [numero]
        elif isinstance(numero, polinomio):
            coefs2=numero.coefs
            
        else:
            raise ValueError("Lo siento, pero no es posible realizar la division")

        while len(listita)>=len(coefs2):
            diferencia=len(listita)-len(coefs2)
            numero_a_multiplicar= listita[-1]/coefs2[-1]
            lista=[0]*(diferencia+1)
            lista[-1]=numero_a_multiplicar
            clase=polinomio(len(lista)-1,lista)
            resta=clase*numero
            coeficientes=coeficientes-resta
            listita=coeficientes.coefs
            cantidad=len(listita)
            for posicion, number in enumerate(listita[::-1]):
                if round(number,4)==0.0: 
                    listita.pop(cantidad-(posicion+1))
                else:
                    break
        if len(listita)==0:
            listita=[0]
        return self.__class__(len(listita)-1,listita)
    def __rmod__(self,numero):
        if isinstance(numero, int) or isinstance(numero, float):
            resultado=[2]
        else:
            raise ValueError("Lo siento, pero no es posible realizar la division")
        if len(resultado)==0:
            resultado=[0]
        return self.__class__(len(resultado)-1,resultado)
    def derivadas (self):
        poli_nuevo=[0]*self.n
        for potencia, numero in enumerate( self.coefs):
            agregar=numero*potencia
            posicion=potencia-1
            poli_nuevo[posicion]+=agregar  
        return self.__class__(len(poli_nuevo)-1,poli_nuevo)
    def rootfind (self,tolerancia=3,x0=0,iteraciones=0):
        y0=sum (self.coefs[i] *x0**i for i in range(len(self.coefs )))
        if round(y0,4)==0.0 or round(y0,4)==0:
            return x0

        f_prima= self.derivadas()
        f_primax0=sum (f_prima.coefs[i] *x0**i for i in range(len(f_prima.coefs )))
        x1= x0-(y0/f_primax0)
        if iteraciones>1000:
            return None
        iteraciones+=1
        raiz=self.rootfind(tolerancia,x1,iteraciones)
        if raiz!=None:  
            return round(raiz,tolerancia)
        
                
    def findroot(self):
        raices={}
        coeficientes=self
        while len(raices) !=self.n:
            raiz= coeficientes.rootfind()
            if raiz==None:
                break
            if raiz not in raices:
                raices[raiz]=1
            else:
                raices[raiz]+=1
            dividendo= polinomio(1,[-raiz,1])
            division=coeficientes//dividendo
            coeficientes=division
        lista_de_tuplas=[]
        if len(raices)==0:
            lista_de_tuplas=coeficientes.coefs
        else:
            for clave in raices:
                tupla=(clave,raices[clave])
                lista_de_tuplas.append(tupla)
        
        return lista_de_tuplas
    def factorize(self):
        coeficiente_principal=self.coefs[-1]
        posicion=len(self.coefs)
        while coeficiente_principal==0:
            posicion=posicion-1
            coeficiente_principal[posicion-1]
            if posicion==0:
                print("0")
                break

        lista_de_tuplas=self.findroot()
        if type(lista_de_tuplas[0])==tuple:
            print(coeficiente_principal,"*",end="")
            posicion=0
            for tupla in lista_de_tuplas:
                if tupla[0]<0:
                    print("(x+",-tupla[0],")**",tupla[1],end="")
                else:
                    print("(x-",tupla[0],")**",tupla[1],end="")
                if posicion!=(len(lista_de_tuplas)-1):
                    print("*",end="")
                    posicion+=1
        else:
            print("Lo siento, pero no se puede factorizar ya que no tiene raices.")
        

        
if __name__=="__main__":
    
    coefs=[-2,1,3]
    n=len(coefs)-1

    a=polinomio(n,coefs)
    b=polinomio(2,[-1,0,1])
    # print((a+b).coefs)
    # print((2+a).coefs)
    # print((a+2).coefs)
    # print((a-2).coefs)
    # print((2-a).coefs)
    # print((a-b).coefs)
    # print((b*a).coefs)
    # print((a*2).coefs)
    # print((2*a).coefs)
    # print(a(1))
    # print((b//a).coefs)
    # print((a//2).coefs)
    # print((2//a).coefs)
    # print((a%b).coefs)
    # print((a%2).coefs)
    # print((2%a).coefs)
    # print(a.derivadas().coefs)
    print(a.rootfind(4))
    print(a.findroot())### mejorar la parte de que te queden raices enteras. 
    (a.factorize())
    # a.get_expression()
    # a.poly_plt(-1,1,color="blue",label= "Poly")