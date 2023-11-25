""""
Write a Python program to create a Pie plot to get the frequency of the three species of the Iris data 
(Use iris.csv) 
Write a Python program to view basic statistical details of the data.(Use wineequality-red.csv)
"""""






import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('iris.csv')

count=df['Species'].value_counts()

plt.pie(count, labels= count.index)

plt.title('Pie plot for iris')
plt.show()

df1=pd.read_csv('winequality-red.csv')

sd=df1.describe()

print("Statistical details of the data are \n",sd)
