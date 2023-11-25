""""
A) Generate a random array of 50 integers and display them using a line chart, scatter plot. 
Apply appropriate color, labels and styling options. [5]
B) Create two lists, one representing subject names and the other representing marks obtained in 
those subjects. Display the data in a pie chart. [5]
C) Write a program in python to perform following task (Use winequality-red.csv ) [5]
Import Dataset and do the followings:
a) Describing the dataset
b) Shape of the dataset
c) Display first 3 rows from dataset

"""

#---A---
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

arr= np.random.randint(1,60,size=50)

#lineplot
plt.plot(arr, color="red", marker="^")
plt.title("LinePlot")
plt.show()

#scatterplot
plt.scatter(range(len(arr)), arr, color='blue', marker='*' )
plt.title("ScatterPlot")
plt.show()

#---B---
sub=['OS','TCS','JAVA','WEBTECH']
marks=[92,60,94,95]

plt.pie(marks, labels =sub)
plt.title("Pie plot for marks!")
plt.show()

#---C---
import pandas as pd

df=pd.read_csv('winequality-red.csv')
print(df)

print("\n\nDescription of the data set is \n",df.describe())
print("\nShape of the dataset is \n", df.shape)
print("\nFirst three rows \n",df.head(3))