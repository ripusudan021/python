# Rows and Column - Operations[Add,update,delete]
import pandas as pd

df = pd.read_csv("test_Data.csv")
print(df)

# Add new column
# df['salary'] = [50000,55000,60000,45000,70000]
# print(df)

df['bonus'] = df['salary']*0.2
print(df)

df.loc[len(df)] = ['jordan',19,'raipur',60000,(60000*0.2)]
print(df)

print(len(df))

df.loc[3,'salary'] = 50000
df.loc[3,'bonus'] = df.loc[3,'salary']*0.2
print(df.iloc[3])

df.loc[len(df)] = ['user',25,'mumbai',62000,(62000*0.2)]
print(df)

print(df.loc[6])
df.drop(df[df.name == "user"].index,inplace=True)#delete row where name is user , axis =0
df.drop(6,axis= 0,inplace=True)
print(df)

df.drop('bonus',axis=1,inplace=True) #delete a column, Axis=1
print(df)

#sort value
print(df.sort_values('salary'))


df.to_csv('test_Data.csv',index=False)
