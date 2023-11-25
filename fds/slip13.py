""""
Write a Python program to create a graph to find relationship between the petal length and petal width.
(Use iris.csv dataset) [10]
Write a Python program to find the maximum and minimum value of a given flattened
array.
"""

#from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
#---A---
df=pd.read_csv('iris.csv')

x=df['PetalLengthCm']
y=df['PetalWidthCm']

plt.plot(x,y, color='black')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Line Graph')
plt.show()

#---B---
import numpy as np

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])

flatarr=arr.flatten()

print("Flattened Array is : \n",flatarr)

maxval=np.max(flatarr)

minval=np.min(flatarr)

print("\nFlattened array:\n",flatarr)
print("Max Value: ",maxval)
print("Min Value: ",minval)
