import matplotlib.pyplot as plt
import numpy
def parabola_show(xa,xb,n,a,b,c,name):
    x = numpy.arange(xa,xb,n)
    y = a*x**2+b*x+c
    plt.plot(x,y, label=name)
    plt.show()
def hyperbola_show(xa,xb,n,k,name):
    x = numpy.arange(xa, xb, n)
    y = k/x
    plt.plot(x, y, label=name)
    plt.show()
parabola_show(-100,100,1,2,2,2,"Rol")
hyperbola_show(-100,100,1,4,"name")