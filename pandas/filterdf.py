import pandas as pd

df = pd.read_csv("test_Data.csv")

# f =  df['age']>22
# print(f)

# print(df[df['age']>22])

# print(df[(df['age']>=23) & (df['city'] == 'indore')])

print(df.where(df['age']>23,other='none'))