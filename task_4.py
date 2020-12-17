import matplotlib.pyplot as plt
import numpy
def stairs_show(xa,xb,n,name):
    x = numpy.arange(xa,n)
    y = numpy.arange()
    plt.plot(x,y, label=name)
    plt.show()