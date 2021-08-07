# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 14:43:33 2021

@author: Camara
"""

class Account:
    
    def __init__(self,id=0,balance=100,annualInterestRate=0.0):
        
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    
    
    def setID(self,id):
        self.__id = id
    
    def getID(self):
        
        return self.__id
    
    def setBalance(self,balance):
        
        self.__balance = balance
    
    def getBalance(self):
        
        return self.__balance
    
    def setAnnualInterestRate(self,annualInterestRate):
        
        self.__annualInterestRate = annualInterestRate
        
    def getAnnualInterestRate(self):
        
        return self.__annualInterestRate
    
    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate / 100) / 12
    
    def getMonthlyInterest(self):
        
        monthlyInterestRate = self.getMonthlyInterestRate()
        
        return self.__balance * monthlyInterestRate
    
    def withdraw(self,amount):
        
        if self.__balance >= amount:
            
            self.__balance -= amount
    
    def deposit(self,amount):
        
        if amount > 0:
            self.__balance += amount