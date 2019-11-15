# Hurricane visualization

In this task we were given a data set on a hurricane and had to illustrate it. The result of the evaluation was plotted in to
visualization as can be seen below:

![alt text](https://raw.githubusercontent.com/naruchixx/DataVisualization/master/Assignment2/Bildschirmfoto%202017-12-16%20um%2020.08.48.png)
## Techincal set up

In this assignment, we were given different data. The data was proc


These packages were used:
-matplotlib (pip install matplotlib)
-numpy (pip install numpy)
--mpl_toolkits.basemap (installation instruction found here: http://matplotlib.org/basemap/users/installing.html)
--gdal (used by basemap, pip install GDAL) 
--pyproj (used by basemap, pip install pyproj)


the class data basically just the gives us the index 'record' of the given values by going into record and then calling packages.
The structure was done as I did in the assignment 1, with arrays and putting corresponding ones underneath each other.
The index function was provided by the site so i just took it from there.
The values are then just inserted in a grid.
the plotting and colouring of the whole thing was done with basemaps, the use was given/explained  there.

needed files are:
TC01.bin,
U01.bin,
v01.bin,
w01.bin.
