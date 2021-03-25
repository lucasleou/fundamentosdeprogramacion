#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 07:52:07 2021

@author: lucasvillegas
"""

def cargar_articulos():
    articulos = []
    precios=[]
    for x in range(5):
        art = input('Ingrese el nombre del articulo: ')
        articulos.append(art)
        prec = int(input('Ingrese el precio del articulo: '))
        precios.append(prec)
    return articulos, precios
def imprimir(articulos, precios):
    for x in range(len(precios)):
        print(articulos[x], precios[x])
def precio_mayor(articulos, precios):
    for x in range(len(precios)) :
        if precios[x] == max(precios):
            print(f'El articulo con el precio más grande es {articulos[x]} con un precio de {precios[x]}')
def importe(articulos, precios):
    importe = int(input('Precio del importe: '))
    print('Articulos con un precio menor: ')
    for x in range(len(precios)):
        if precios[x]<= importe:
            print(articulos[x], precios[x])
articulos, precios = cargar_articulos()
imprimir(articulos, precios)
precio_mayor(articulos,precios)
importe(articulos,precios)