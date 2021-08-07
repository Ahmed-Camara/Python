# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:33:09 2021

@author: Camara
"""

from QuadraticEquationClass import QuadraticEquation

a = int(input('Enter value of a : '))
b = int(input('Enter value of b : '))
c = int(input('Enter value of c : '))

Q = QuadraticEquation(a,b,c)

discriminant = Q.getDiscriminant()



if discriminant > 0:
    print('Root 1 : {}\nRoot 2 : {}\n'.format(Q.getRoot1(),Q.getRoot2()))
else:
    print('The equation has no roots')
    
