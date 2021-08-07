# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 15:17:13 2021

@author: Camara
"""

SLOW = 1
MEDIUM = 2
FAST = 3
    
class Fan:
    
    
    
    def __init__(self,speed=SLOW,on=False,radius=5,color='blue'):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
        
    
    def getSpeed(self):
        
        return self.__speed
    
    def setSpeed(self,speed):
        
        self.__speed = speed
    
    def setOn(self,on):
        
        self.__on = on
        
    def getOn(self):
        
        return self.__on
    
    def setRadius(self,radius):
        
        self.__radius = radius
        
    def getRadius(self):
        
        return self.__radius
    
    def setColor(self,color):
        
        self.__color = color
        
    def getColor(self):
        
        return self.__color
    
    def __str__(self):
        
        return "Speed : {}\nRadius : {}\nColor : {}\nTurn on : \n".format(self.__speed,self.__radius,self.__color,self.__on)
        