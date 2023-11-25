""""
Write a Python program to perform the following tasks :
a. Apply OneHot encoding on Country column.
b. Apply Label encoding on purchased column
(Data.csv have two categorical column the country column, and the purchased column).
"""
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import pandas as pd


#---A---
df= pd.read_csv('Data.csv')
ohe= OneHotEncoder(handle_unknown='ignore')
print(ohe)
df=pd.DataFrame(ohe.fit_transform(df[['Country']]).toarray())
print("One Hot Encoding: \n",df)

#---B---
df= pd.read_csv('Data.csv')
label=LabelEncoder()
df['Purchased']=label.fit_transform(df['Purchased'])

print("\nLabel Encoded: \n",df)