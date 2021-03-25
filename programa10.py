#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:02:14 2021

@author: lucasvillegas
"""

def cuadrado():
    x = int(input('Ingrese un número: '))
    cuadrado = x*x
    print(f'El cuadrado de {x} es {cuadrado}')
def producto():
    n1 = int(input('Ingrese un número: '))
    n2 = int(input('Ingrese un número: '))
    prod = n1 * n2
    print(f'El producto de {n1} y {n2} es {prod}')
cuadrado()
producto()