#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:38:06 2021

@author: lucasvillegas
"""

def mult(num, terminos = 10):
    for x in range(terminos):
        i = x * num
        print(i, ',', sep='', end='')
    print()
mult(2)
mult(5,15)
mult(10,15)