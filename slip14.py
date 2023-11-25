""""
Write a Python NumPy program to compute the weighted average along the specified axis
 of a given flattened array.
Write a Python program to view basic statistical details of the data (Use advertising.csv)
"""
#---A---
import numpy as np

arr= np.array([2,4,6,8])
warr= np.array([0.1,0.2,0.3,0.4])

wavg= np.average(arr, weights=warr)

print("Weighted average : \n",wavg)
print('---------------------------------------')

#---B---
import pandas as pd

df=pd.read_csv('Advertising.csv')

desc=df.describe()
print("\nStatistical details of the data are : \n", desc)