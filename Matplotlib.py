# Plotting graphs
# In this folder I researched how my Numpy array can be plotted on a scatter graph using Matplotlib:

# matplotlib.pyplot is renamed as plt
import numpy
# import data into data into array 
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

# I am using maximum and minimum of each column to create the graph
maxall = numpy.max(data[:,0]), numpy.max(data[:,1]), numpy.max(data[:,2]), numpy.max(data[:,3])
minall = numpy.min(data[:,0]), numpy.min(data[:,1]), numpy.min(data[:,2]), numpy.min(data[:,3])
print('The maximum of each column is', numpy.around(maxall, decimals=1))
min1 = numpy.around(minall, decimals=1)
max1 = numpy.around(maxall, decimals=1)

print(max1)
print(min1)

import matplotlib.pyplot as plt
plt.scatter(min1,max1)
plt.xlabel('minimum label')
plt.ylabel('maximum label')
plt.show()
