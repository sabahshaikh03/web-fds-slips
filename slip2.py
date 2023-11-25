""""
A) Write a Python program for Handling Missing Value. Replace missing value of salary,
age column with mean of that column.(Use Data.csv file).
B) Write a Python program to generate a line plot of name Vs salary [5]
C) Download the heights and weights dataset and load the dataset froma given csv file into a dataframe. 
Print the first, last 10 rows and random 20 rows also display shape of the dataset.
"""""

import pandas as pd
import matplotlib.pyplot as plt
#----A----
df=pd.read_csv('Data.csv')
print(df)

salmean= df['Salary'].mean()
agemean= df['Age'].mean()

#print("\nMean salary is \n",salmean)
#print("\nMean age is \n",agemean)
df['Salary'].fillna(salmean, inplace =True)
df['Age'].fillna(agemean, inplace=True)

print("\nData frame without null values : \n",df)
print("----------------------------------------------")


#----B----
print("B)LINE PLOT")
plt.plot(df['Country'],df['Salary'], color='red', marker='^')
plt.xlabel('Country')
plt.ylabel('Salary')
plt.show()

print("----------------------------------------------")

#----C----
df1=pd.read_csv('SOCR-HeightWeight.csv')
print("First 10 rows: \n")
print(df1.head(10))
print("\nLast 10 rows: \n")
print(df1.tail(10))
print("\nRandom 20 rows:\n")
print(df1.sample(20))
print("\nDataset Shape: ",df1.shape)

print("----------------------------------------------")
