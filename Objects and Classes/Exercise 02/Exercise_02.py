# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 14:08:28 2021

@author: Camara
"""

from StockClass import Stock

stock = Stock(symbol='INTC',name='Intel Corporation')

stock.setpreviousClosingPrice(20.5)
stock.setCurrentPrice(20.35)

print(stock.getChangePercent())