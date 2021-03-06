# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:27:32 2021

@author: Camara
"""

import time
import random

class StopWatch:
    def __init__(self):
        self.__startTime = time.time()

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime
    
    def start(self):
        self.__startTime = time.time()
    
    def stop(self):
        self.__endTime = time.time()
    
    def getElapsedTime(self):
        return int(1000 * (self.__endTime - self.__startTime))
    

if __name__ == '__main__':
    size = 1000000

    stopWatch = StopWatch()
    sum = 0    
    for i in range(1, size + 1):
      sum += i 
    stopWatch.stop()
    
    print("The loop time is", stopWatch.getElapsedTime(), "milliseconds") 