# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 18:50:32 2023

@author: Usuario
"""

class myarray:
    def __init__(self,elems,r,c,by_row):
        self.elems=elems
        self.r=r
        self.c=c
        self.by_row=by_row
    def get_pos(self,j,k):
        if len(self.elems)==self.r*self.c:
            if self.by_row:
                m=j*self.c+k
            else:
                m=k*self.r+j
            return m
    def get_coords(self,position):
        if len(self.elems)==self.r*self.c:
            if self.by_row:
                k= position%self.c
                j= (position-k)//self.c
            else:
                k=position//self.r
                j=position%self.r
            return j,k
    def switch(self):
        lista=[]
        position=0
        
        if self.by_row:
            while position!=c:
                lista.extend(self.elems[position::self.c])
                position+=1
                byrow=False
        else:
            while position!=r:
                lista.extend(self.elems[position::self.r])
                position+=1
                byrow=True
        return myarray(lista,self.r,self.c,byrow)
    def get_elem (self,j,k):
        posicion=self.get_pos(j,k)
        return self.elems[posicion]
    def get_row (self,j):
        if not self.by_row:
            lista=self.switch().elems
        else:
            lista=self.elems
        fila=list(lista[j*self.c:j*self.c+self.c])
        return fila
    def get_col (self,k):
        if self.by_row:
            lista=self.elems
        else:
            lista=self.switch().elems
        columna=lista[k::self.c]
        return columna
    def del_row (self,j):
        if  self.by_row:
            copia= self.elems.copy()
        else:
            copia=self.switch().elems.copy()
            
        lista=copia[:j*self.c]+copia[self.c*j+self.c:]

        return lista
    def del_col(self,k):
        if  self.by_row:
            copia= self.elems.copy()
        else:
            copia=self.switch().elems.copy()
        for numero in range(k, len(copia)+1,self.c-1):
            copia.pop(numero)
            if numero==len (copia):
                break
        return copia
    def añadir (self,intercambio,k,fila):
        
        posicion= k*self.c
        for numero in fila:
            intercambio.insert(posicion,numero)
            posicion+=1
        
    def swap_rows (self,j,k):
        #siempre sea j mayor que k
        filaj= self.get_row(j)
        filak=self.get_row(k)
        eliminacion= (self.del_row(j))
        array= (myarray(eliminacion,self.r,self.c,self.by_row))
        intercambio=array.del_row(k)
        self.añadir(intercambio,k,filaj)
        self.añadir(intercambio, j, filak)
        return intercambio
        
r=4
c=3
by_row=True
elems=[0,2,4,
       6,2,4,
       5,6,0,
       7,8,9]
j=2
k=1
my_array=myarray(elems, r, c, by_row)

#print(my_array.get_pos( j, k))
#print(my_array.get_coords(9))
#print(my_array.switch().switch().elems)
#print(my_array.get_row(3))
#print(my_array.get_col(2))
#print(my_array.del_row(2))
#print(my_array.del_col(2))
print (my_array.swap_rows(j, k))