# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:41:07 2021

@author: Camara
"""

from TimeClass import Time


if __name__ == '__main__':
    
    currentTime = Time()
    print("Current time is " + str(currentTime.getHour()) + ":" + str(currentTime.getMinute()) + ":" + str(currentTime.getSecond()))

    elapseTime = eval(input("Enter the elapse time: "))
    currentTime.setTime(elapseTime)
    print("The hour:minute:second for elapse time is " + str(currentTime.getHour()) + ":" + str(currentTime.getMinute()) + ":" + str(currentTime.getSecond()))
