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
# The answer gave me an idea of the average of each sepal and petal and its' lenght and width. 

# I will try to resuse the code from above however I will try to make it simpler; less repetition. Then I will use it to calculate teh maximum and minimum. 

# to measure minimum of each column I can use below column.
'''minall = numpy.min(data[:,0:4])''' # this was an error because it summed everything up when I needed seperate values

minall = numpy.min(data[:,0]), numpy.min(data[:,1]), numpy.min(data[:,2]), numpy.min(data[:,3])
print('The minimum of each column is', numpy.around(minall, decimals=1))
# The result: The minimum of each column is [ 4.3  2.   1.   0.1]

# without the numpy around it was giving me a more accurate decimal on the minimum column but it works good now

# to calculate the maximum of each column I have used 'numpy.max(data)'
maxall = numpy.max(data[:,0]), numpy.max(data[:,1]), numpy.max(data[:,2]), numpy.max(data[:,3])
print('The maximum of each column is', numpy.around(maxall, decimals=1))
#the result: The maximum of each column is [ 7.9  4.4  6.9  2.5]
