# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:50:08 2023

@author: Usuario
"""
#%%
#Ejercicio lets make a deal
import random
def letsmakeadeal(eleccion):
    tesoro= random.randint(1,3)
    cabras = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    cabras[tesoro].remove(random.choice(cabras[tesoro]))
    if eleccion==tesoro:
        eleccion_nueva=cabras[tesoro]
    else: 
        eleccion_nueva=tesoro
    if eleccion_nueva== tesoro:
        resultado=("Ganaste")
    else: 
        resultado=("Perdiste")
    return resultado
contador=0
resultados={"Ganaste":0,"Perdiste":0}
while contador!=100:
    eleccion=random.randint(1,3)
    partida=letsmakeadeal(eleccion)
    resultados[partida]+=1
    contador+=1
#%% 
import string
import random



#def chequeo (password, encriptacion, seed="50d858e0985ecc7f60418aaf0cc5a"):
    
    
    
def encriptar (password, seed="50d858e0985ecc7f60418aaf0cc5a"):
    random.seed(seed)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    diccionario={}
    for elemento in password:
        valor= random.sample(caracteres,5)
        diccionario[elemento]=valor
    encriptacion=""
    for Value in diccionario.values():
        encriptacion+= random.choice (Value)
 #   return(chequeo(password, encriptacion))


#x=encriptar ("echi" )
#print(chequeo("echi", x))
#%%
class usuario:
    cantidad_usuarios=0
    def __init__ (self,nombre,apellido,mail, password):
        self.nombre=nombre
        self.apellido= apellido
        self.mail=mail
        self.password=password
        ID=usuario.cantidad_usuarios+1
        usuario.cantidad_usuarios+1
    def encriptar (password, seed="50d858e0985ecc7f60418aaf0cc5a"):
        random.seed(seed)
        caracteres = string.ascii_letters + string.digits + string.punctuation
        diccionario={}
        for elemento in password:
            valor= random.sample(caracteres,5)
            diccionario[elemento]=valor
        encriptacion=""
        for Value in diccionario.values():
            encriptacion+= random.choice (Value)    
    # def chequeo()
    
    
    
    
    
    
    