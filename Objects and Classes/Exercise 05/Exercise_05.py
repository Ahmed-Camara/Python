# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:12:22 2021

@author: Camara
"""

from RegularPolygonClass import RegularPolygon


reg1 = RegularPolygon(6,4)

reg2 = RegularPolygon(10, 4, 5.6, 7.8)


print("Polygon 1 : \nArea : {}\nPerimeter : {}\n".format(reg1.getArea(),reg1.getPerimeter()))

print("Polygon 2 : \nArea : {}\nPerimeter : {}\n".format(reg2.getArea(),reg2.getPerimeter()))