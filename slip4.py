""""
Generate a random array of 50 integers and display them using a line chart, scatter plot, histogram and
box plot. Apply appropriate color, labels and styling options. 

Write a Python program to print the shape, number of rows-columns, data types, feature names and 
the description of the data(Use User_Data.csv)

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("A\n")
df=np.random.randint(1,100, size=50)
print(df)

#line chart
plt.plot(df,color='red')
plt.title('Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

#Scatter 
plt.scatter(range(50),df,color='green',marker='*')
plt.title('Scatter Chart')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

#Histogram
plt.hist(df,color='yellow', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#BoxPlot
plt.boxplot(df)
plt.title('Box Plot')
plt.xlabel('Value')
plt.show()
print("-------------------------------------")

#----B----
df1= pd.read_csv('User_Data.csv')

print("Shape of the data : \n",df1.shape)
print("\nNumber of rows: \n",df1.shape[0])
print("\nNumber of columns: \n",df1.shape[1])
print("\nData Type: \n",df1.dtypes)
print("\nFeature Names: \n", df1.columns)
print("\nDescription of data :\n", df1.describe())