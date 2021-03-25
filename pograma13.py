#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:02:15 2021

@author: lucasvillegas
"""

def mayor_edad(edad, *edades):
    may_18 = 0
    if edad >= 18:
        may_18 = may_18+1
    for x in range(len(edades)):
        if edades[x] >= 18:
            may_18 = may_18 +1
    return may_18
print('Cantidad de edades mayor a 18', mayor_edad(1,30,20,4,12,55,30,21))