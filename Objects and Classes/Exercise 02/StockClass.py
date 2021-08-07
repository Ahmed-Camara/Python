# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 14:09:15 2021

@author: Camara
"""

class Stock:
    
    def __init__(self,symbol='',name=''):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = 0.0
        self.__currentPrice = 0.0
    
    def getStockName(self):
        
        return self.__name
    
    def getStockSymbol(self):
        
        return self.__symbol
    
    def getpreviousClosingPrice(self):
        
        return self.__previousClosingPrice
    
    def setpreviousClosingPrice(self,previousClosingPrice):
        
        self.__previousClosingPrice = previousClosingPrice
        
    def getCurrentPrice(self):
        
        return self.__currentPrice
    
    def setCurrentPrice(self,currentPrice):
        
        self.__currentPrice = currentPrice
    
    def getChangePercent(self):
        
        return (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice
    
    def __str__(self):
        
        return "Stock name = {}\n Stock Symbol = {}\nPrevious Closing price = {}\nCurrent Price = {}\n".format(self.__name,self.__symbol,self.__previousClosingPrice,self.__currentPrice)