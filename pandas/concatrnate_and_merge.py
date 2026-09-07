import pandas as pd

df1 = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Rahul", "Priya", "Amit", "Neha", "Vikas"],
    "age": [25, 28, 22, 30, 26],
    "city": ["Indore", "Bhopal", "Delhi", "Indore", "Mumbai"]
})

# print(df1)

df2 = pd.DataFrame({
    "id": [1, 2, 3, 6, 7],
    "salary": [35000, 42000, 30000, 50000, 45000],
    "department": ["IT", "HR", "Sales", "IT", "Finance"]
})

# print(df2)

# merged_df = pd.concat([df1,df2],axis = 0) # vertical/row level/top on top
merged_df = pd.concat([df1,df2],axis = 1) # vertical/row level/top on top
# print(merged_df)

print(pd.merge(df1,df2,how="inner",on='id'))
print(pd.merge(df1,df2,how="left",on='id'))
print(pd.merge(df1,df2,how="right",on='id'))
print(pd.merge(df1,df2,how="outer",on='id'))