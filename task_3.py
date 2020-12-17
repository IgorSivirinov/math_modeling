import matplotlib.pyplot as plt
import numpy
def circle_show(xa,xb,n,R,name):
    x = numpy.arange(xa, xb, n)
    y = x+n
    X, Y = numpy.meshgrid(x, y)
    f_xy = X ** 2 + Y ** 2
    plt.contour(X, Y, f_xy, levels=[R**2])
    plt.axis('equal')
    plt.show()
def ellipse_show(xa, xb,n, a,b, R, name):
    x = numpy.arange(xa, xb, n)
    y = numpy.arange(xa, xb, n)
    X, Y = numpy.meshgrid(x, y)
    f_xy = X**2*a**2 + Y**2*b**2
    plt.contour(X, Y, f_xy, levels=[R ** 2])
    plt.axis('equal')
    plt.show()
circle_show(-100,100,1,90,"name")
ellipse_show(-100,100,3,2,1,100,"nn")