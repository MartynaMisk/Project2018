# Project2018 

## *This respitory was created for a project which concerns Fisher's Iris Data Set.*
> Fisher's Iris data set that can be found in this [data folder](https://github.com/MartynaMisk/Project2018/blob/master/data/irisdata.csv).

### The content of the respitory is as follow: 
- Background Infromation
- Investigation steps
  - Investigating *NumPy*
   - Investigating *SciPy*
    - Investigating *Matplotlib*
     - Investigating *Pandas*
- Summary
- References     

### Background information 

In 1936 a British statistician and biologist named Ronald Fisher published a paper called 'The use of multiple measurements in taxonomic problems' where he introduced the Fisher's Iris Data Set. The data set consist of 50 samples from each of three species of Iris; *Setosa, Versicolor & Virginica*. The [data](https://github.com/MartynaMisk/Project2018/blob/master/data/irisdata.csv) contains 150 records under 5 species which are organized into five columns **Sepal length, Sepal Width, Petal Length, Petal Width and Species** measured in centimetres. 

This data set is often used for testing out machine learning algorithms and visualizations graphs. 
In this Project I will try to evaluate the Iris Data Set by calculate the mean, max and minimum of each column by using different Python libraries; this can be found under '*Investigation steps*' of this README.md. I will also take a deeper investigation on creation of graphs using code and briefly evaluate my findings. I believe this project will be greatly beneficial to me as I get to explore a completely new side to programming, data analysis and use Github platform which is relatively new to me.

![Pic](http://www.painters-online.co.uk/ugc-1/fullnews/news/16492/9864_big.jpg)
## Investigation steps
> Investigating NumPy

Firstly, I will calculate the *mean*, *maximum* and *minimum* of each column using library **NumPy** through programme **ipython**. Sample code can be seen below, more information in folder [NumPy.py](https://github.com/MartynaMisk/Project2018/blob/master/NumPy.py). 
In the folder you will find a code usign NumPy to first calculate the mean of each column, then I will investigate how I can calculate the minimum and maximum of each column. This will give me an idea of new code and also gives me insight information into the data which is not visible only by looking at.
```ruby

meanfirstcolumn = numpy.mean(data[:,0])
minfirstcolumn = numpy.min(data[:,0])

```
> Investigating SciPy

**SciPy** stands for Scientific Python. SciPy is built on NumPy and ...... will use another library called panda where we will arrive at similar results but usign different programms.
```ruby
sample code to organize data?
or sample code to measure mean 
panda

```
> Investigating Matplotlib

I have used **Matplotlib** / Pylab to for plotting hte grpahs. Below is a snapshot of the code, more information on the code and explaantions can be found in [matplotlib.py]().
```ruby
sample code to organize data?
or sample code to measure mean 
panda

```
> Investigating Pandas

I have then investigated how I can used Pandas for structured data operations and manipulations. Below is an example. more detailed information can be found in [panda.py]
Scatterplots for example:

### Summary of the investigation 
Explain with what code 'loop' & 'for statment' you were able to calculate the mean, max and minimum of each column. I was bale to seperate the columns into each specy identigying the ... 

### References
- [Wikepedia](https://en.wikipedia.org/wiki/Iris_flower_data_set) Information on the background of Iris DataSet
- [UCI Machine Learning Repository:Iris Data Set](https://archive.ics.uci.edu/ml/datasets/iris) Additional information on analysis
- [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/) Examples of python code and how its used to investigate dataset
- [Numerical Python Course](https://www.python-course.eu/numpy.php) Additional study on Python and its libraries
- [Iris Flower Painting](http://www.painters-online.co.uk/techniques-and-tips/view,botanical-painting-for-beginners-how-to-paint-an-iris-in-watercolour-with-jarnie-godwin_16492.htm)
- google
- stackflow 
- other links
