#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:40:20 2021

@author: lucasvillegas
"""

def vocales(palabra):
    cont_vocales= 0
    for x in palabra.lower():
        if x== 'a' or x== 'e' or x=='i' or x=='o'or x=='u':
            cont_vocales = cont_vocales+1
    print(f'En la palabra {palabra} hay {cont_vocales} vocales')
vocales("Palabra")
vocales('hola')
vocales('Adios')