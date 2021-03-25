#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:02:15 2021

@author: lucasvillegas
"""

def multiplicar(lista, escalar):
    for x in range(len(lista)):
        lista[x] = lista[x]*escalar
    print(lista)
                

lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)