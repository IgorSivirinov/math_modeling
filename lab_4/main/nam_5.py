import numpy
CIRCLE = 1
RECTANGLE = 2
TRIANGLE = 3
def area(figure,side=0, height=0, radius=0):
    if(figure == CIRCLE):
        return numpy.pi*radius**2
    elif(figure == RECTANGLE):
        return side*height
    elif(figure == TRIANGLE):
        return  side*height/2
