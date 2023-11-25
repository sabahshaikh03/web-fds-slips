""""
Write a program in python to perform following task :
Standardizing Data (transform them into a standard Gaussian distribution with 
a mean of 0 and a standard deviation of 1) (Use winequality-red.csv)
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

df=pd.read_csv('winequality-red.csv')

print("Oringinal Data: \n",df)
cols=df.columns

#cols=['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide',
#'total sulfur dioxide','density','pH','sulphates','alcohol','quality']

scaler=StandardScaler()

df[cols]=scaler.fit_transform(df[cols])
print("Standardized data : \n",df)