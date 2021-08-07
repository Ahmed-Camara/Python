# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:55:16 2021

@author: Camara
"""

class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
    
    def isSolvable(self):
        
        return ((self.__a * self.__d) - (self.__b * self.__c)) != 0
    
    def getX(self):
        
        num = ((self.__e * self.__d) - (self.__b * self.__f))
        den = ((self.__a * self.__d) - (self.__b * self.__c))
        
        if den == 0:
            return 0
        return num / den
    
    def getY(self):
        num = ((self.__a * self.__f) - (self.__e * self.__c))
        den = ((self.__a * self.__d) - (self.__b * self.__c))
        if den == 0:
            return 0
        return num / den
    