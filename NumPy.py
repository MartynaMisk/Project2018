#Martyna Miskiewicz
# First attempt at analyzing the data using Numpy. 
# NumPy stands for Numerical Python which contains a powerful n-dimensional array object or arrays can be also called tables.
# In this folder I will investigate how I can calculate the mean, maximum and minumum of ech column. This will give me measurements to understand the Iris flower in more detail.
# I will use builed in library NumPy which is new to me. I came across errors when I have used it in ipython and then trying to using it in the python envirement. 
# I was able to finally figure out that I need the print() code to finalize the code.

# Calculte mean of each column 
import numpy 
# import data into data into array 
data = numpy.genfromtxt('data/iris.csv', delimiter=',')
# measure the mean of each column using numpy.mean and by giving each column different name and replacing the data to each column it represents
meanfirstcolumn = numpy.mean(data[:,0])
meansecondcolumn = numpy.mean(data[:,1])
meanthirdcolumn = numpy.mean(data[:,2])
meanfourthcolumn = numpy.mean(data[:,3])
# using print() to ensure the answer is given to me in python
print('The mean of the Sepal Lenght column is', meanfirstcolumn)
print('The mean of the Sepal Width column is', meansecondcolumn)
print('The mean of the Petal Lenght column is', meanthirdcolumn)
print('The mean of the Petal Width column is', meanfourthcolumn)
