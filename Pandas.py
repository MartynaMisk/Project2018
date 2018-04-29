# I will use Pandas code to plot a histogram.
# Pandas is usually used for visualization of data.
import pandas

import matplotlib.pyplot as plt

'''dataset = pandas.read_csv('data/iris.csv')'''
# This code abovve gives me the histogram I am looking for however it is not clear as its not label properly.
# I will now investigate how I can insert 'petal length petal width etc.'

dataset = pandas.read_csv('data/iris.csv', names = ["Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width", "non-existent"])
# I have overcame the prolem by inserting a fith name of the column 'non-existent' 
# to insert a histogram 
# You can see the histogram in README.md

dataset.hist()

plt.show()
