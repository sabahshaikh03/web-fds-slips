""""
Write a python program to create two lists, one representing subject names and the other representing marks 
obtained in those subjects.
Display the data in a pie chart and bar chart.

Write a python program to create a data frame for students information such as name,
 graduation percentage and age. 
Display average age of students, average of graduation percentage.
"""

#---A---


import matplotlib.pyplot as plt

sub= ['OS','TCS','WEBTECH','JAVA','PYTHON']
marks= [91,85,94,90,97]

#piechart

plt.pie(marks, labels=sub)
plt.title("Pie Chart")
plt.show()

#bargraph
plt.bar(sub,marks, color='yellow', edgecolor='black')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Bar Graph')
plt.show()

#---B---
import pandas as pd
import numpy as np

data={ 'Name':['Saba','Dayanand','Anurag','Parshuram','Shireen'],
       'Gradper':[92,94,89,87,91],
       'Age':[20,19,20,19,19]
       }
df=pd.DataFrame(data)
print(df)
print(df['Age'].mean())
avg_age=np.average(df['Age'])
print("\nAverage age of students is: \n",avg_age)

avg_per=np.average(df['Gradper'])
print("Average percentage of students is: \n",avg_per)
