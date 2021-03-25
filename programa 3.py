#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:47:16 2021

@author: lucasvillegas
"""

#variables
#contador de repeticiones
cont_rep = 1
#cuadrado de la suma 
cua_sum = 0
#acumulado de la suma
acu_sum = 0 

cant_num = int(input("ingrese la cantidad de numeros : "))

while cont_rep <= cant_num:
    cua_sum = cont_rep * cont_rep
    acu_sum = acu_sum + cua_sum
    print("el cuadrado de : ",cont_rep,"es : ",cua_sum)
    print("la suma de los cuadrados es : ",acu_sum)
    cont_rep = cont_rep +1

