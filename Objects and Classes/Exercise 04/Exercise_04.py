# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 15:10:56 2021

@author: Camara
"""

from FanClass import Fan

SLOW = 1
MEDIUM = 2
FAST = 3

fan1 = Fan(FAST,True,10,'Yellow')

fan2 = Fan(MEDIUM,False,5,'Blue')

print('Fan 1 : \n {}'.format(fan1))

print()

print('Fan 2 : \n {}'.format(fan2))