""""
1.To create a dataframe containing columns name, age and percentage.
Add 10 rows to the dataframe. View the dataframe.
2. To print the shape, number of rows-columns, data types, feature names and the description of the data
3. To Add 5 rows with duplicate values and missing values. Add a column ‘remarks’ with empty values.
Display the data.
"""
#1
import pandas as pd
data={ 'Name':[   ],
       'Age':[  ],
       'Sal':[  ],
       'Dept':[  ]  }

df=pd.DataFrame(data)
df.loc[0]=['Saba',22,1000000,'Fin']
df.loc[1]=['Dj',21,2000000,'Acc']
df.loc[2]=['Parssu',20,70000,'Mark']
df.loc[3]=['Shireen',22,69000,'Fin']
df.loc[4]=['Anurag',20,89000,'Acc']
df.loc[5]=['Kiran',22,90000,'Sales']
df.loc[6]=['Rahul',21,100000,'Mark']
df.loc[7]=['Rohan',22,89000,'Sales']
df.loc[8]=['Hitesh',21,95000,'Acc']
df.loc[9]=['Pratiksha',21,75000,'Fin']

print(df)

#2

print("Shape :\n", df.shape)
print("Number of rows:  ",df.shape[0])
print("Number of columns:  ", df.shape[1])
print("Datatypes:\n", df.dtypes)
print("Features of DataFrame: \n",df.columns)
print("Description of data\n", df.describe())

#3

df.loc[10]=['Saba',22,1000000,'Fin']
df.loc[11]=['Isha',22,None,'Fin']
df.loc[12]=['Madhura',22,1000000,None]
df.loc[13]=['Dj',21,2000000,'Acc']
df.loc[14]=['Shivani',None,1000000,'Fin']
df['remarks']=None

print("\n\nData frame with null and duplicate values: \n\n",df)


    