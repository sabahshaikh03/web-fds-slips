""""
Write a python program to Display column-wise mean, and median for SOCR-HeightWeight dataset.
Write a python program to compute sum of Manhattan distance between all pairs of points.
"""

import pandas as pd

#---A---
df=pd.read_csv('SOCR-HeightWeight.csv')

mean=df.mean()
print("Mean is \n",mean)

median=df.median()
print("Median is \n", median)

#---B---
