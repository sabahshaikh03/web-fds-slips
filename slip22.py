""""
Dataset Name: winequality-red.csv [15]
Write a program in python to perform following tasks
a. Rescaling: Normalised the dataset using MinMaxScaler class
b. Standardizing Data (transform them into a standard Gaussian distribution
 with a mean of 0 and a standard deviation of 1)
c. Normalizing Data ( rescale each observation to a length of 1 (a unit norm).
 For this, use the Normalizer class.)
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler 

#---a---
df=pd.read_csv('winequality-red.csv')
cols=df.columns
#cols=['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide',
#'total sulfur dioxide','density','pH','sulphates','alcohol','quality']

scale_1=MinMaxScaler()
df[cols]=scale_1.fit_transform(df[cols])
print("Rescaled Dataframe\n",df)

#---b---
scale_2=StandardScaler()
df[cols]=scale_2.fit_transform(df[cols])
print("\n\nStandardized Dataframe\n",df)

#---c---
scale_3=Normalizer()
df[cols]=scale_3.fit_transform(df[cols])
print("\n\nNormalized Dataframe\n",df)






