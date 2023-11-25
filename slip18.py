""""
A)Write a Python program to create box plots to see how each feature 
i.e. Sepal Length, Sepal Width, Petal Length, Petal Width are distributed across the three species.
 (Use iris.csv dataset)
B)Use the heights and weights dataset and load the dataset from a given csv file into a dataframe. 
Print the first, last 5 rows and random 10 row
"""

#---A---
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('iris.csv')

df.boxplot(column=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'], by='Species')
#plt.title('BoxPLot')
plt.show()

#---B---

df1=pd.read_csv('SOCR-HeightWeight.csv')
print("First five rows: \n", df1.head(5))
print("\nLast five rows: \n", df1.tail(5))
print("\nRandom 10 rows: \n", df1.sample(10))