import pandas as pd

df = pd.read_csv("test_Data.csv")
#Rows & Column - Selection
print(df)

# Column Selection
print(df[['name']])#single column
print(df[["name",'age','city']])#multiple column

#Row Selection

#Loc - label based index
print(df.loc[(df.name=='alex')])
print(df.loc[(df.name=='alex') | (df.name == 'bob')])
print(df.loc[1:4]) #last index is included

#iloc - index value based
print(df.iloc[2])
print(df.iloc[2:4]) #last index is excluded