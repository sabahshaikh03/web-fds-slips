""""
Write a Python program to draw scatter plots to compare two features of the iris dataset.
Write a Python program to create a data frame containing columns name, age , salary, department . 
Add 10 rows to the data frame. View the data frame.
"""
#---A---

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('iris.csv')

plt.scatter(df['SepalLengthCm'],df['SepalWidthCm'], color= 'green', marker='*')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title("Scatter Plot")
plt.show()

#---B---
data={ 'Name':[   ],
       'Age':[  ],
       'Sal':[  ],
       'Dept':[  ]  }

df=pd.DataFrame(data)
df.loc[0]=['Saba',22,1000000,'Fin']
df.loc[1]=['Dj',21,1000000,'Acc']
df.loc[2]=['Parssu',20,1000000,'Mark']
df.loc[3]=['Shireen',22,1000000,'Fin']
df.loc[4]=['Anurag',20,1000000,'Acc']
df.loc[5]=['Kiran',22,1000000,'Sales']
df.loc[6]=['Rahul',21,1000000,'Mark']
df.loc[7]=['Rohan',22,1000000,'Sales']
df.loc[8]=['Hitesh',21,1000000,'Acc']
df.loc[9]=['Pratiksha',21,1000000,'Fin']

print(df)
    