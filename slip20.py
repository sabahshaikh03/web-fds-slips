""""
Generate a random array of 50 integers and display them using a line chart, 
scatter plot, histogram and box plot. Apply appropriate color, labels and styling options. [10]

Add two outliers to the above data and display the box plot.
"""

#A done already

#---B---
import numpy as np
import matplotlib.pyplot as plt

df=np.random.randint(1,70,size=50)

print(df)

outliers=[150,280]
df=np.concatenate([df,outliers])
plt.boxplot(df)
plt.show()


