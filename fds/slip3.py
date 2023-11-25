""""
A)Write a Python program to create box plots to see how each feature i.e. 
Sepal Length, Sepal Width, Petal Length, Petal Width are distributed across the three species. 
(Use iris.csv dataset) 
B) Write a Python program to view basic statistical details of the data (Use Heights and Weights Dataset)

"""

import pandas as pd
import matplotlib.pyplot as plt
print("BOXPLOT")
df=pd.read_csv("iris.csv")
df.boxplot(column=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'], by='Species')
plt.xlabel("Features")
plt.ylabel("Centimeters")
plt.title("Box Plot")
plt.show()
print("------------------------------------")

df1= pd.read_csv('SOCR-HeightWeight.csv')
print("\n Statistical details of the data are : \n", df1.describe())
print("------------------------------------")
