# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:54:32 2021

@author: Camara
"""
from LinearEquationClass import LinearEquation


a = int(input('Enter value of a : '))
b = int(input('Enter value of b : '))
c = int(input('Enter value of c : '))
d = int(input('Enter value of d : '))
e = int(input('Enter value of e : '))
f = int(input('Enter value of f : '))

linearE = LinearEquation(a,b,c,d,e,f)

print(linearE.getY())
if linearE.isSolvable():
    print('X is {}\nand Y is {}: '.format(linearE.getX(),linearE.getY()))
else:
    print('The equation has no solution')