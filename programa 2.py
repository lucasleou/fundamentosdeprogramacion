#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:29:34 2021

@author: lucasvillegas
"""
#variables 
#acumulado de la suma 
sum_acum = 0
#cuadrdo de la suma
cua_sum = 0
cant_nums = int(input("ingrese la cantidad de numeros : "))

for cont in range (cant_nums + 1):
    cua_sum = cont * cont 
    sum_acum = sum_acum + cua_sum
    print("el cuadrado de : ",cont, "es : ",cua_sum)
    print("la suma acumulada es : ", sum_acum)

