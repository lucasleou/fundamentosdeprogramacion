#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 07:38:06 2021

@author: lucasvillegas
"""

suma_potencias = 0
cant_num = int(input("ingrese la cantidad de numeros que quiere operar : "))
for x in range(cant_num):
    if x > 0:
        exp = 10 ** x
        suma_potencias = suma_potencias + exp
        print(exp)
print(f'Suma total: {suma_potencias}')