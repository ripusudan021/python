import pandas as pd
import numpy as np

df = pd.read_csv("test_Data.csv")
# df.drop(['Unnamed: 0.1',"Unnamed: 0"],axis=1,inplace=True)
# print(df)

# df.to_csv('test_Data.csv',index=False)

print(df.isnull())
df.loc[df.name == 'sam','salary'] = np.nan
print(df.isnull().sum())
print(df.fillna(0))

