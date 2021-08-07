class Rectangle:
    
    def __init__(self,width = 1,height = 2):
        self.__width = width
        self.__height = height
    
    
    def setWidth(self,width):
        self.__width = width
    
    
    def getWidth(self):
        return self.__width
    
    
    def setHeight(self,height):
        self.__height = height
    
    def getHeight(self):
        return self.__height
    
    def getArea(self):
        return self.__width * self.__height
    
    
    def getPerimeter(self):
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        return "The rectangle has a width of : {} and an height of : {}".format(self.__width,self.__height)