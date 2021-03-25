#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 07:52:08 2021

@author: lucasvillegas
"""

suma = 0
cant_num = int(input('Digite la cantidad de números:  ')) +1
for x in range(cant_num):
    exp = x ** 2
    suma = suma + (exp)
    print(f'El cuadrado de {x} es {exp}\n La suma acumulada es {suma}')    
print(f'La suma final es {suma}')