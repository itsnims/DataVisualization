import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import ListedColormap


class Data(object):
    def __init__(self, category):
        self.__data = self.getPackage(category)
#return the data as a numpy array so we can use its contents
    def getPackage(self, category):
        return np.fromfile(category + "01.bin", dtype='>f')

    def getIndex(self, x, y, z):
#find the datarecord in the datalist
        index = self.__data[x + 500* (y + 500 * z)]
#was given on the website
        if index < 1000:
            return index
        return self.getIndex(x+1, y, z)


def CONTOUR(data, ax):
#find z value according to hight in meters
    mincolour = 100000
    maxcolour = -100000

    z = 8
    matrix = []

    list = range(500)
    for x in list:
        matrix.append([])
        for y in list:  #the exact same structure i did in assignment 1 with the arrays
            point = data.getIndex(x, y, z)
            matrix[x].append(point)

        #hanging on all the variables for x..like 1,1  1,2  1,3 etc
        if min(matrix[x]) < mincolour:
            mincolour = min(matrix[x])
        if max(matrix[x]) > maxcolour:
            maxcolour= max(matrix[x])
        #need the minimum and maximum of all for the coloring



    #the following codes are given functions under the matplotlib basemaps examples
    contourmap = Basemap(projection='mill', resolution="l", llcrnrlat=23.7, llcrnrlon=-83, urcrnrlat=41.7, urcrnrlon=-62)
    contourmap.bluemarble()
    contourmap.drawcoastlines()
    contourmap.drawstates()
    x, y = np.meshgrid(np.linspace(0, contourmap.urcrnrx, 500), np.linspace(0, contourmap.urcrnry, 500))
    interval = (maxcolour - mincolour) / 20
    steps = np.arange(mincolour, maxcolour, interval)
    color = plt.cm.RdYlGn
    t_color = color(np.arange(color.N))
    t_color = ListedColormap(t_color)
    map = ax.contourf(x,y, matrix, levels=steps, cmap=t_color)
    return map




def WIND(x, y, z, ax):

    value = 5

    data_u = []
    data_v = []
    data_w = []

    for xachse in range(20):
        for yachse in range(20):
            data_u.append(xachse+x.getIndex((25)*xachse, (25)*yachse, value))
            data_v.append(yachse+y.getIndex((25)*xachse, (25)*yachse, value))
            data_w.append(z.getIndex((25) * xachse, (25) * yachse, value))

#the following functions are again given by matlabplotlib basemaps examples
    windmap = Basemap(projection='mill', resolution="l", llcrnrlat=23.7, llcrnrlon=-83, urcrnrlat=41.7, urcrnrlon=-62)
    windmap.bluemarble()
    windmap.drawcoastlines()
    windmap.drawstates()
    color=plt.cm.RdYlGn
    a,b = np.meshgrid(np.linspace(0, windmap.urcrnrx, 20), np.linspace(0, windmap.urcrnry, 20)) #makes a grid with 20 points 'arrows'
    map = ax.quiver(a,b, data_u, data_v, data_w, cmap=color)
    return map
