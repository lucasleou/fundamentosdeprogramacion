#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:38:09 2021

@author: lucasvillegas
"""

def sup_rect(lado1,lado2):
    superficie = lado1*lado2
    return superficie
l1 = int(input('Ingrese un lado: '))
l2 = int(input('Ingrese un lado: '))
if l1 > l2:
    print(f'{l1} es el lado mayor')
else:
    print(f'{l2} es el lado mayor')
print('La superficie de este rectángulo es: ', sup_rect(l1,l2))