# Project2018 

## *This repository was created for a project which concerns Fisher's Iris Data Set.*
> Fisher's Iris data set that can be found in this [data folder](https://github.com/MartynaMisk/Project2018/blob/master/data/irisdata.csv). This folder consiste .csv comma-seperated values of Iris measurements.

### The content of the respitory is as follow: 
- Background Infromation
- Investigation steps
  - Investigating *NumPy*
   - Investigating *Matplotlib*
    - Investigating *Pandas*
- Summary
- References     

### Background information 

In 1936 a British statistician and biologist named Ronald Fisher published a paper called 'The use of multiple measurements in taxonomic problems' where he introduced the Fisher's Iris Data Set. The data set consist of 50 samples from each of three species of Iris; *Setosa, Versicolor & Virginica*. The [data](https://github.com/MartynaMisk/Project2018/blob/master/data/irisdata.csv) contains 150 records under 5 species which are organized into five columns **Sepal length, Sepal Width, Petal Length, Petal Width and Species** measured in centimetres. I have tested it by applying following code:

```ruby
import numpy
data = numpy.genfromtxt('data/iris.csv', delimiter=',')
print('Iris Dataset contains', data.shape[0],'rows and', data.shape[1], 'columns.')
# I used [0] to first shows data for rows and then [1] to show columns only. 
# Otherwise it would appear like this: (150,5) and I wanted to add text.
```

This flat file(which is either .txt /.csv) dataset is often used for testing out machine learning algorithms and visualizations graphs. 
In this Project I will try to evaluate the Iris Data Set by calculate the mean, maximum and minimum of each column by using different Python libraries; this can be found under '*Investigation steps*' of this README.md. I will also reserach the creation of graphs using Matplotlib and Pandas then briefly evaluate my findings. I believe this project will be greatly beneficial to me as I get to explore a completely new side to programming, data analysis and use Github platform which is relatively new to me.

![Pic](http://www.painters-online.co.uk/ugc-1/fullnews/news/16492/9864_big.jpg)
## Investigation steps
> Investigating NumPy

Firstly, I will calculate the *mean*, *maximum* and *minimum* of each column using library **NumPy** through programme **ipython**. Sample code can be seen below, more information in folder [NumPy.py](https://github.com/MartynaMisk/Project2018/blob/master/NumPy.py). 
In the folder you will find a code usign NumPy to first calculate the mean of each column, then I will investigate how I can calculate the minimum and maximum of each column. This will give me an idea of new code and also gives me insight information on analyzing the iris dataset.

```ruby
import numpy 
data = numpy.genfromtxt('data/iris.csv', delimiter=',')
meanfirstcolumn = numpy.mean(data[:,0])
minfirstcolumn = numpy.min(data[:,0])

```
While investigating above, I have came across code that can analyze only two columns of the data. I can use that to quicly evaluate different sepal length and petal lenght.

```ruby
import numpy 
data = numpy.loadtxt('data/iris.csv', delimiter=',', usecols=[0,2])
print(data)

```

> Investigating Matplotlib

I have used **Matplotlib** to research how I can plot graphs. Below is a snapshot of the code I have used to plot the minimum and maximum of **Sepal length, Sepal Width, Petal Length and Petal Width**. More information on code in [Matplotlib.py](https://github.com/MartynaMisk/Project2018/blob/master/Matplotlib.py). I have included a screenshot Python has given me.

```ruby
import matplotlib.pyplot as plt
plt.scatter(min1,max1)
plt.xlabel('minimum label')
plt.ylabel('maximum label')
```

![scatterplotminmax](https://user-images.githubusercontent.com/36375583/39400352-929a22aa-4b26-11e8-80c8-d733d8206d1f.PNG)
*I have learned how to import photos from my desktop by dragging the photo to issue(header above) andd then copying the url.*

> Investigating Pandas

I have then researched how I can use **Pandas** for structured data operations and manipulations. I want to store data into Histogram hene I will use Panda. Below is an example, more detailed information can be found in [panda.py](https://github.com/MartynaMisk/Project2018/blob/master/Pandas.py)
The result of the Histogram:

![nameshistogram](https://user-images.githubusercontent.com/36375583/39407721-6c98946e-4bc2-11e8-8942-52e4f41bc4b9.PNG)

```ruby
import pandas
import matplotlib.pyplot as plt
```

### Summary of the investigation 
I have learned that NumPy is libraray for Python for storing numerical data. It's efficient, clean and fast. Secondly, they are othen essencial for other packages. Numpy has a build in functions that allow us to easly import data as arrays. I have learned the definiton of flatfiles using Numpy and how I can structure graphs using code. I was able to calculate the mean, maximum and minimum of each column. I have first developed a simple but not so user friendly hence I have worked on simplyfing it. I was able to seperate the columns as I wanted to only compare two columns Sepal lenght and Peta Lenght instead of having four columns. Then, I went to learning more about Matplotlib and Pandas. I have learned that I can create a scatterplot using Matplotlib and I was able to create Histrogram using Pandas. Overall, I found this project very interesting and I got to discover new libraries for Python and how they can be used for different purposes. 

### References
- [Wikepedia](https://en.wikipedia.org/wiki/Iris_flower_data_set) Information on the background of Iris DataSet
- [UCI Machine Learning Repository:Iris Data Set](https://archive.ics.uci.edu/ml/datasets/iris) Additional information on analysis
- [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/) Examples of python code and how its used to investigate dataset
- [Numerical Python Course](https://www.python-course.eu/numpy.php) Additional study on Python and its libraries
- [Iris Flower Painting](http://www.painters-online.co.uk/techniques-and-tips/view,botanical-painting-for-beginners-how-to-paint-an-iris-in-watercolour-with-jarnie-godwin_16492.htm)
- [Histogram code](https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342) Simple way of plotting a histogram

## THE END
