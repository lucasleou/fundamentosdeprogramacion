#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 09:48:35 2021

@author: lucasvillegas
"""

def sumarizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may


def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men
    

# bloque principal del programa

lista=[10, 56, 23, 120, 94]
print("La lista completa es")
print(lista)
print("La suma de todos su elementos es", sumarizar(lista))
print("El mayor valor de la lista es", mayor(lista))
print("El menor valor de la lista es", menor(lista))