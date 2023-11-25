""""
A) Generate a random array of 50 integers and display them using a line chart, scatter plot, 
histogram and box plot. Apply appropriate color, labels and styling options. 
B) Write a Python program to create data frame containing column... name,
 salary, department add 10 rows with some missing and duplicate values to the data frame.
 Also drop all null and empty values. Print the modified data frame.
"""
#A is completed in slip4

#---B---

import pandas as pd
data={ 'Name':['abc','pqr','tuv','lmn','stu','opq','jkl','def','efg','rst'],
     'Sal':[1000000,None,60000,None,95000,None,67000,40000,30000,60000],
     'Dept':['Fin','Fin',None,'Sales','Acc','Sales','Acc',None,'Fin','Acc']  }
df=pd.DataFrame(data)
print("Dataframe with null values\n",df)
df.loc[10]=['jkh',809000,'Sales']

df=df.dropna()
print("\n\n\nDataframe after dropping null values\n",df)


