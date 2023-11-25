""""
A) Import dataset “iris.csv”. Write a Python program to create a Bar plot to get the 
frequency of the three species of the Iris data. 
B)Write a Python program to create a histogram of the three species of the Iris data.
"""

from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('iris.csv')
#bar graph
species_count=df['Species'].value_counts()
print(species_count)

plt.bar(species_count.index,species_count, color='yellow', edgecolor='black')
plt.title('Bar graph')
plt.xlabel('species')
plt.ylabel('frequency')
plt.show()

#histogram
#DID NOT COMPLETELY UNDERSTAND CHAT GPT KA CODE HAI
# Create histograms for each species
plt.hist([df[df['Species']=='Iris-setosa']['SepalLengthCm'],
          df[df['Species']=='Iris-versicolor']['SepalLengthCm'],
          df[df['Species']=='Iris-virginica']['SepalLengthCm']],
         bins=10, alpha=0.7, label=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], color=['red', 'green', 'blue'])

# Add labels and title
plt.title('Histogram of Sepal Length for Each Iris Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Count')

# Show the plot
plt.show()