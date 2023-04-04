# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 18:50:32 2023

@author: Usuario
"""

class myarray:
    """ La clase toma una matriz en forma de lista y reliza emtodos en esta de acuerdo a lo pedido."""
    
    
    def __init__(self,elems,r,c,by_row):
        """
        

        Parameters
        ----------
        elems : una lista con los elementos de la matriz
        r : int
            numero de filas en la matriz
        c : int
            numero de columnas.
        by_row : bool
            Menciona si la matriz esta ordenada por filas o columnas.

        Returns
        -------
        None.

        """
        self.elems=elems
        self.r=r
        self.c=c
        self.by_row=by_row
    def get_pos(self,j,k):
        """
        

        Parameters
        ----------
        j : fila
        k : columna.

        Returns
        -------
        m : posicion de acuerdo a una fila y una columna.

        """
        if len(self.elems)==self.r*self.c:
            if self.by_row:
                m=j*self.c+k
            else:
                m=k*self.r+j
            return m
    def get_coords(self,position):
        """
        

        Parameters
        ----------
        position : El numero de posicion del cual se van a buscar las coordenadas.

        Returns
        -------
        j : fila.
        k : columna

        """
        if len(self.elems)==self.r*self.c:
            if self.by_row:
                k= position%self.c
                j= (position-k)//self.c
            else:
                k=position//self.r
                j=position%self.r
            return j,k
    def switch(self):
        """
        Cambia el by_row de la matriz

        """
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
        """Devuelve el elemento en la posición (j,k) de la matriz."""
        posicion=self.get_pos(j,k)
        return self.elems[posicion]
    def get_row (self,j):
        """Devuelve la fila j de la matriz."""
        if not self.by_row:
            lista=self.switch().elems
        else:
            lista=self.elems
        fila=list(lista[j*self.c:j*self.c+self.c])
        return fila
    def get_col (self,k):
        """Devuelve la columna k de la matriz."""
        if self.by_row:
            lista=self.elems
        else:
            lista=self.switch().elems
        columna=lista[k::self.c]
        return columna
    def del_row (self,j):
        """Elimina la fila j de la matriz y devuelve la matriz resultante como una lista."""
        if self.by_row:
           copia = self.elems.copy()
        else:
           copia = self.switch().elems.copy()

        lista = copia[:j*self.c]+copia[self.c*j+self.c:]
        return myarray(lista,self.r,self.c,self.by_row)# cambiado
    def del_col(self,k):
        """Elimina la columna k de la matriz y devuelve la matriz resultante como una lista."""
        if  self.by_row:
            copia= self.elems.copy()
        else:
            copia=self.switch().elems.copy()
        for numero in range(k, len(copia)+1,self.c-1):
            copia.pop(numero)
            if numero==len (copia):
                break
        return myarray(copia,self.r,self.c,self.by_row)#cambiado
    def añadir (self,intercambio,k,fila):
        """Añade los elementos de la fila indicada en la matriz intercambio a partir de la posición k."""
        posicion= k*self.c
        for numero in fila:
            intercambio.elems.insert(posicion,numero)
            posicion+=1
        
    def swap_rows (self,j,k):
        """Intercambia las filas j y k de la matriz y devuelve la matriz"""
        filaj = self.get_row(j)
        filak = self.get_row(k)
        eliminacion = (self.del_row(j))
        intercambio = eliminacion.del_row(k)
        self.añadir(intercambio, k, filaj)
        self.añadir(intercambio, j, filak)
        return intercambio
    
    def swap_cols (self,l,m):
        """Intercambia las columnas l y m de la matriz y devuelve la matriz
        """
        if not by_row:
            copia=self.switch().elems.copy()
        else:
            copia=self.elems.copy()            
        mayor=max(l,m)
        menor=min (l,m)
        columna1= self.get_col(mayor)
        columna2=self.get_col(menor)
        posicion1=mayor
        posicion2=menor
        for elemento in columna2:
            copia[posicion1]=elemento
            posicion1=posicion1+self.c
        for elemento in columna1:
            copia[posicion2]=elemento
            posicion2=posicion2+self.c
        return myarray(copia,self.r, self.c, self.by_row)    
    def scale_row(self,j,x):
        """Multiplica todos los elementos de la fila j de la matriz por el escalar x y devuelve la matriz. """
        if by_row:
            copia= self.elems.copy()
        else: 
            copia=self.switch().elems.copy()
        fila= self.get_row(j)
        posicion=j*self.c
        for elemento in fila:
            copia[posicion]=elemento*x
            posicion+=1
        return myarray(copia,self.r,self.c,self.by_row)
    def scale_col (self,k,y):
        """
        Multiplica todos los elementos de la columna k de la matriz por el escalar y y devuelve la matriz.

        """
        if by_row:
            copia= self.elems.copy()
        else: 
            copia=self.switch().elems.copy()
        columna= self.get_col(k)
        posicion=k
        for elemento in columna:
            copia[posicion]=elemento*y
            posicion+=self.c
        return myarray(copia,self.r,self.c,self.by_row)
    
    def transpose(self):
        """Devuelve la matriz transpuesta"""
        lista=[]
        position=0
        
        if self.by_row:
            while position!=c:
                lista.extend(self.elems[position::self.c])
                position+=1
        else:
            while position!=r:
                lista.extend(self.elems[position::self.r])
                position+=1
        return myarray(lista,self.r, self.c, self.by_row)
    
    def flip_cols (self):
        """
        

        Returns
        -------
        copia : Una lista con los elementos de la columna puestos de atras para adelante

        """

        if self.by_row:
            copia=self.elems.copy()
        else:
            copia=self.switch().elems.copy()
        copia=self
        lista=list(range(self.c))
        for elemento in lista:
            copia=copia.swap_cols(elemento, lista[-1])
            lista=lista[1:-1]
            if len(lista)<=1:
                break
        return copia
                
    def flip_rows (self):
        """
        

   
        copia : una lista con las filas puestas de atras para adelante.

        """
        if self.by_row:
            copia=self.elems.copy()
        else:
            copia=self.switch().elems.copy()
        copia=self
        lista=list(range(self.r))
        for elemento in lista:
            copia=copia.swap_rows(elemento, lista[-1])
            lista=lista[1:-1]
            if len(lista)<=1:
                break
        return copia

    def achicar(self,fila,columna):
        """
        sirve para achicar la matriz en la recursividad

        Parameters
        ----------
        fila : la fila a eliminar
        columna : la columna a eliminar

        Returns
        cambia la lista a un objeto con una lista reducida

        """
        lista=[]
        for elemento in range(len(self.elems)):
            j,k= self.get_coords(elemento)
            if j!= fila and k!=columna:
                lista.append(self.elems[elemento])
        return myarray(lista, self.r-1, self.c-1, self.by_row)
    def det(self):
        """
        

        Realiza el determinante de una matriz usando una recursividad que va achicando la matriz

        """
        if self.r != self.c:
            print("La matriz tiene que ser cuadrada")
            return None
        if self.r == 2:
            determinante = self.elems[0]*self.elems[3] - self.elems[1]*self.elems[2]
            return determinante
        else: 
            determinante=0
            for n in range(self.r):
                recursividad = (-1)**n * self.elems[n] * self.achicar(0, n).det()
                determinante += recursividad
            return determinante
  


    def __matmul__(self,my_arrayz):

        lista=[]
        for i in range(self.r):
            mult1= self.get_row(i)
            for fila in range (my_arrayz.c):
                sumar=0
                for param in range(self.r):
                    mult2=my_arrayz.get_col(fila)
                    sumar+=mult1[param]*mult2[param]
                lista.append(sumar)
               
        return lista
    def __mul__(self,escalar):
        lista=[]
        for x in self.elems:
            lista.append(x*escalar)
        return lista
    def __rmul__(self,escalar):
        lista=[]
        for x in self.elems:
            lista.append(x*escalar)
        return lista
    def del_row2(self,k):
        identidad=myarray(eye(self.c).delete_rows(k),self.r-1,self.c,self.by_row)
        matriz= myarray(elems,self.r,self.c,self.by_row)
        return identidad@matriz
    def del_col2(self, k):
        identidad=myarray(eye(self.c).delete(k),self.r,self.c-1,self.by_row)
        matriz= myarray(elems,self.r,self.c,self.by_row)
        mult=matriz@identidad
        return mult
    def swap_col2(self,j,k):
        identidad=myarray(eye(self.c).swap(j,k),self.r,self.c,self.by_row)
        matriz= myarray(elems,self.r,self.c,self.by_row)
        mult=matriz@identidad
        return mult
    def swap_rows2 (self,j,k):
        identidad=myarray(eye(self.c).swap(j,k),self.r,self.c,self.by_row)
        matriz= myarray(elems,self.r,self.c,self.by_row)
        return identidad@matriz
    def __add__(self,numero):
        matriz= [numero]*self.c*self.r
        lista=[]
        for x in list(map(list,zip(matriz,self.elems))):
            lista.append(sum(x))
        return lista

    def __radd__(self,numero):
        matriz= [numero]*self.c*self.r
        lista=[]
        for x in list(map(list,zip(matriz,self.elems))):
            lista.append(sum(x))
        return lista
    def __sub__(self, numero):
        matriz= [-numero]*self.c*self.r
        lista=[]
        for x in list(map(list,zip(matriz,self.elems))):
            lista.append(sum(x))
        return lista
    def __rsub__(self,numero):
        lista=[]
        for x in (self.elems):
            lista.append(numero-x)
        return lista


    def cofactor(self):
        """
        Calcula el determinante de una matriz

        Returns
        -------
        det : Determinante

        """
        lista=[]
        if self.r != self.c:
            print("La matriz debe ser cuadrada")
            return None
        if self.r == 2:
            det = self.elems[0]*self.elems[3] - self.elems[1]*self.elems[2]

        if self.r > 2:
            det = 0
            for j in range(len(self.elems)):
                # calcula el cofactor para cada elemento en la primera fila
                #entra a este if hasta que r=2. i siempre es 0. 
                x,y=self.get_coords(j)
                cofactores = (-1)**j * self.elems[j] * self.achicar(x, y).det()
                det += cofactores
                lista.append(det)
                det=0
        return lista
    def inversa(self):
        matriz=my_array.cofactor()
        det=my_array.det()
        transpuesta=myarray(matriz, self.r, self.c, self.by_row).transpose()
        return (1/det)*transpuesta


 

class eye ():
    def __init__(self,c):
        self.c=c
    def create(self):
        identidad= [0]*self.c*self.c
        for posicion in range(0,len(identidad),self.c+1):
            identidad[posicion]=1
        
        return identidad
    
    def delete(self,d):
        identidad=self.create()
        lista=[]
        posicion=d
        for i in range(len(identidad)):
            if i!=posicion:
                lista.append(identidad[i])
            else:
                posicion+=self.c
        
        return lista
    def delete_rows(self,d):
        lista=self.create()
        posicion=d*self.c
        lista=lista[0:posicion]+lista[posicion+c::]
        return lista
    def swap (self,a,b):
        identidad= self.create()
        identidad[self.c*a+a]=0
        identidad[self.c*a+b]=1
        identidad[self.c*b+a]=1
        identidad[self.c*b+b]=0
        return identidad















class myarray2:
    def __init__(self,elems,r,c,by_row):
        """Inicializa un objeto de la clase myarray con los siguientes parámetros:
            elems: la lista  de listas que representa la matriz.
            r: la cantidad de filas de la matriz.
            c: la cantidad de columnas de la matriz.
            by_row: indica si la lista representa la matriz por filas o por columnas."""
        self.elems=elems
        self.r=r
        self.c=c
        self.by_row=by_row    
    def get_pos(self,j,k):
        if self.by_row:
            m=j*self.c+k
        else:
            m=k*self.r+j
        return m    
    def get_coords(self,position):
        if self.by_row:
            k= position%self.c
            j= (position-k)//self.c
        else:
            k=position//self.r
            j=position%self.r     
        return j,k
    def switch(self):
        """
        Cambia el by_row de la matriz

        """
        lista=[]
        if self.by_row:
            for elemento in range(self.r):
                lista_chica=[]
                for posicion in range(self.c):
                    lista_chica.append(self.elems[posicion][elemento])
                lista.append(lista_chica)
            by_row=False
        else:
            for elemento in range(self.c):
                lista_chica=[]
                for posicion in range(self.r):
                    lista_chica.append(self.elems[posicion][elemento])
                lista.append(lista_chica)
            by_row=False
        return myarray2(lista, self.r, self.c, by_row)

    def get_row(self,j):
        """Devuelve la fila j de la matriz."""

        if self.by_row:
            fila= self.elems[j]
        else:
            listanueva=my_array2.switch().elems
            fila=listanueva[j]
        return fila
    def get_col(self,k):
        """Devuelve la columna k de la matriz."""

        if not self.by_row:
            columna= self.elems[k]
        else:
            listanueva=my_array2.switch().elems
            columna=listanueva[k]
        return columna
        
    def get_elem (self,j,k):
        """Devuelve el elemento en la posición (j,k) de la matriz."""

        if self.by_row:
            elemento= self.elems[j][k]
        else:           
            elemento= self.elems[k][j]
        return elemento

    def del_row(self,j):
        """Elimina la fila j de la matriz y devuelve la matriz resultante como una lista."""

        if self.by_row:
            copia=self.elems.copy()
            copia.pop(j)
        else:
            copia=my_array2.switch().elems.copy()
            copia.pop(j)
        return myarray2(copia, self.r, self.c, by_row)

    def del_col (self,k):
        """Elimina la columna k de la matriz y devuelve la matriz resultante como una lista."""

        lista_nueva=[]
        if  self.by_row:
            copia=self.elems.copy()
        else:
            copia=my_array2.switch().elems.copy()
        for listita in copia:
            posicion=0
            mini_lis=[]
            for elemento in range (self.r):
                if posicion!=k:
                    mini_lis.append(listita[posicion])
                posicion+=1
            lista_nueva.append(mini_lis)
        return myarray2(lista_nueva, self.r, self.c, self.by_row)
    
    def swap_rows(self,j,k):
        """Intercambia las filas j y k de la matriz y devuelve la matriz"""

        lista=[]
        mayor=max(j,k)
        menor=min(j,k)
        lista_mayor= self.get_row(mayor)
        lista_menor=self.get_row(menor)
        posicion=0
        if self.by_row:
            for listita in self.elems:
                if posicion== menor:
                    lista.append(lista_mayor)
                elif posicion==mayor:
                    lista.append(lista_menor)
                else:
                    lista.append(listita)
                posicion+=1
        else:
            for listita in my_array2.switch().elems:
                if posicion== menor:
                    lista.append(lista_mayor)
                elif posicion==mayor:
                    lista.append(lista_menor)
                else:
                    lista.append(listita)
                posicion+=1
        return myarray2(lista,self.r, self.c, self.by_row)
    def swap_cols(self,l,m):
        """Intercambia las columnas l y m de la matriz y devuelve la matriz
        """
        if self.by_row:
            copia= self.elems.copy()
        else:
            copia=my_array2.switch().elems.copy()
        for listita in copia:
            cambio1=listita[l]
            cambio2=listita[m]
            listita[l]=cambio2
            listita[m]=cambio1
        return myarray2(copia,self.r, self.c, self.by_row)
    def scale_row(self,j,x):
        """Multiplica todos los elementos de la fila j de la matriz por el escalar x y devuelve la matriz. """

        if self.by_row:
            copia=self.elems.copy()
        else:
            copia=my_array2.switch().elems.copy()
        lista_añadir=[]
        for numero in copia[j]:
            multiplicar=numero*x
            lista_añadir.append(multiplicar)
        copia[j]=lista_añadir
        return myarray2(copia,self.r, self.c, self.by_row)
            
    def scale_col(self,k,y):
        """
        Multiplica todos los elementos de la columna k de la matriz por el escalar y y devuelve la matriz.

        """
        if self.by_row:
            copia=self.elems.copy()
            for listita in copia:
                listita[k]=listita[k]*y
            
        else:
            copia=my_array2.scale_row(k, y).elems.copy()
        return myarray2(copia,self.r, self.c, self.by_row)
        
    def flip_rows(self):
        """
        

   
        copia : una lista con las filas puestas de atras para adelante.

        """
        if self.by_row:
            copia=self.elems.copy()[::-1]
        else:
            copia=self.switch().elems.copy()
            posicion=0
            for listita in copia:
                listita=listita[::-1]
                copia[posicion]=listita
                posicion+=1
        return myarray2(copia,self.r, self.c, self.by_row)
    def flip_cols(self):
        """
        

        Returns
        -------
        copia : Una lista con los elementos de la columna puestos de atras para adelante

        """
        if self.by_row:
            copia=self.elems.copy()
            posicion=0
            for listita in copia:
                listita=listita[::-1]
                copia[posicion]=listita
                posicion+=1
        else:
            copia=self.switch().elems.copy()[::-1]
        return myarray(copia,self.r, self.c, self.by_row)
    def transpose (self):
        """Devuelve la matriz transpuesta"""
        lista=[]
        if self.by_row:
            for elemento in range(self.r):
                lista_chica=[]
                for posicion in range(self.c):
                    lista_chica.append(self.elems[posicion][elemento])
                lista.append(lista_chica)
        else:
            for elemento in range(self.c):
                lista_chica=[]
                for posicion in range(self.r):
                    lista_chica.append(self.elems[posicion][elemento])
                lista.append(lista_chica)
        return myarray2(lista, self.r, self.c, self.by_row)
    def achicar(self,fila,columna):
        """
        sirve para achicar la matriz en la recursividad

        Parameters
        ----------
        fila : la fila a eliminar
        columna : la columna a eliminar

        Returns
        cambia la lista a un objeto con una lista reducida

        """
        x=self.del_row(fila)
        lista=x.del_col(columna)
        return myarray(lista, self.r-1, self.c-1, self.by_row)
    def det(self):
        """
        

        Realiza el determinante de una matriz usando una recursividad que va achicando la matriz

        """
        if self.r != self.c:
            print("La matriz tiene que ser cuadrada")
            return None
        elif self.r==1:
            return self.elems[0]
        else:
           
            if self.r == 2:
                determinante = self.elems[0][0]*self.elems[1][1] - self.elems[0][1]*self.elems[1][0]
                return determinante
            else: 
                determinante = 0
                for n in range(self.r):
                    recursividad = (-1)**n * self.elems[n] * self.achicar(0, n).det()
                    determinante += recursividad
                return determinante
        

        
        
        
        
        
        
            


if __name__=='__main__':
    # elems=[[0,1,2],[
    #         3,4,5],[
    #         6,7,8]]
    # r=3   
    # c=3
    # by_row=True

    # j=2
    # k=1
    # m=2
    # l=1
    # x=3
    # y=3
    # my_array2=myarray2(elems, r, c, by_row)

    # print(my_array2.get_pos(j, k))
    # print(my_array2.get_coords(m))
    # print(my_array2.switch().switch().elems)
    # print (my_array2.get_row(j))
    # print (my_array2.get_col(k))
    # print (my_array2.get_elem(j, k))
    # print(my_array2.del_row(j).elems)
    # print(my_array2.del_col(k).elems)
    # print(my_array2.swap_rows(j, k).elems)
    # print (my_array2.swap_cols(l, m).elems)
    # print (my_array2.scale_row(j,x).elems)
    # print(my_array2.scale_col(k,y).elems)
    # print (my_array2.flip_rows().elems)
    # print(my_array2.flip_cols().elems)
    # print(my_array2.transpose().transpose().elems)
    r=3   
    c=3
    by_row=True

    j=2
    k=1
    m=2
    l=1
    x=3
    y=3
    elems = [1, 2, 3,
              3, 2, 1,
              1, 0, 1]
    my_array=myarray(elems, r, c, by_row)
    # print(my_array.get_pos( j, k))
    # print(my_array.get_coords(9))
    # print(my_array.switch().switch().elems)
    # print(my_array.get_row(2))
    # print(my_array.get_col(2))
    # print(my_array.del_row(2).elems)
    # print(my_array.del_col(2).elems)
    # print (my_array.swap_rows(j, k).elems, )
    # print(my_array.swap_cols(l, m).elems)
    # print(my_array.scale_row(j, x).elems)
    # print(my_array.scale_col(k, y).elems)
    # print(my_array.transpose().transpose().elems)
    # print(my_array.flip_cols().elems)
    # print (my_array.flip_rows().elems)
    # print(my_array.det())
    # elems2=[0,1,2,3,4,5]
    # r2=3
    # c2=2
    # by_row2=True
    # print(my_array.cofactor())
    # print(2-my_array)
    # print(my_array.inversa())
    # print(my_array.del_row2(2))
    # print(my_array.del_col(2).elems)
    #print(my_array.swap_col2(1, 2))
    print(my_array.swap_rows2(1,2))











