import pandas as pd
df = pd.read_csv("test_Data.csv")

# print(df['age'].value_counts()) #gives frequency

print(df.groupby('age')['salary'].mean())
print(df.groupby('age')['salary'].sum())

print(df.groupby('age').agg({'salary':'mean','name':"count"}))