# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:39:08 2023

@author: Usuario
"""
#%%   ejercicio 173 de la guia
#%% Ejercicio 173 de la guia

def valores ():
    num= (input("Elija un numero o enter si no desea continuar"))
    if num =="":
        return 0
    else:
        num=int(num)
        return num+ valores()

Total= valores()
if Total==0:
    Total=0.0
print("el numero total es: ", Total )

#%%  ejercicio 174 de la guia
def euclides (a,b):
    if b==0:
        return 0
    else:
        c=a%b
        if c!=0:
            a,b=b,c
            euclides(a, b)
        else:
            print("el MCD es : ", b)            
            return b
a= int(input("Ingrese el numero a que sea el mayor"))
b= int(input("Ingrese el numero b que sea menor que a"))
if a>b:
    euclides(a, b)

else: 
     print("No hay MCD ya que b es mayor que a")

#%% ejercicio 176 de la guia
diccionario={"A": "Alpha", "B": "Bravo", "K": "Kilo", "T": "Tango", 
             "C" :"Charlie","L": "Lima", "U": "Uniform",
             "D": "Delta", "M" :"Mike", "V": "Victor" , 
             "E" :"Echo" ,"N" :"November" ,"W": "Whiskey",
             "F": "Foxtrot", "O": "Oscar", "X": "Xray",
             "G" :"Golf", "P": "Papa" ,"Y": "Yankee",
             "H" :"Hotel" ,"Q" :"Quebec" ,"Z" :"Zulu",
             "I": "India","R": "Romeo","J" :"Juliet", "S": "Sierra"}
word= input("Elige una palabra")
word=word.upper()
def NATO (diccionario,word):
    if len(word)!=1:
        Tail= word[1::]
        letra1= word[0]
        return diccionario[letra1] +" "+ NATO(diccionario,Tail)+" "
    else:
        letra1=word
        return diccionario[letra1]
x=NATO(diccionario, word)
print(x)
#%% Ejercicio 180 de la guia
string1= input("Ingrese el string 1: ")
string2= input("Ingrese el string 2: ")
distancia=0
def distancia_de_strings(St1,St2,distancia):
    c1= len(St1)
    c2=len(St2)
    if c1==1 or c2==1:
        if St1[0]!=St2[0]:
            distancia+=1
        if c1>c2:
            distancia+=c1-c2
        if c2>c1:
            distancia+=c2-c1
        print( "La distancia es: ",distancia )   
        return distancia         
    tail1=St1[1::]
    tail2=St2[1::]
    if St1[0]!=St2[0]:
        distancia+=1
    distancia_de_strings(tail1, tail2,distancia)
distancia_de_strings(string1, string2, distancia)
