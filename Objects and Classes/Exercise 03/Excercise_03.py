# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 14:29:47 2021

@author: Camara
"""

from AccountClass import Account

account = Account(1122,20000,4.5)

account.withdraw(2500)

account.deposit(3000)


print("ID = {}".format(account.getID()))

print("Balance = {}".format(account.getBalance()))

print("Monthly Interest Rate = {}".format(account.getMonthlyInterest()))

print("Monthly Interest = {}".format(account.getMonthlyInterest()))