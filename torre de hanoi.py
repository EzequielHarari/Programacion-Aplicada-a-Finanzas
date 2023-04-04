# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:18:53 2023

@author: Usuario
"""
discos=int (input(" inserte la cantidad de discos"))
a=int(input("inserte en que torre arranca"))
movimientos=0
def torre_de_hanoi(discos,a,final):
    global movimientos
    if discos==1:
        movimientos+=1
        print(f"Mover el disco 1 desde {a} hasta {final}")
    else:
        if max(final,a)==min (final,a):
            k=3
        else:
            k=max (final,a)-min(final,a)
        torre_de_hanoi(discos-1, a, k)
        movimientos+=1
        print(f"Mover el disco {discos} desde {a} hasta {final}")
        torre_de_hanoi(discos-1, k, final)
torre_de_hanoi(discos, a, 3)