#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:30:39 2021

@author: lucasvillegas
"""

#definir variables
num = 0
suma = 0 
prom =0.0
can_ele = 0
salida = False

while salida == False:
    num=int(input("dijite su edad mi estimado : "))
    if num > 0:
        suma=suma + num
        can_ele = can_ele + 1
    else:
        salida = True
prom = suma / can_ele
print("la suma del comedio es :", prom)