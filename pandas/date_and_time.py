import pandas as pd

df = pd.read_csv("test_Data.csv")

df['doj'] = [
    "2021-01-15",
    "2022-03-20",
    "2022-07-10",
    "2023-02-25",
    "2024-06-18",
    "2025-09-05"
]
# print(df)
# print(df['doj'].dtype)

df['doj'] = pd.to_datetime(df['doj'])
# print(df.dtypes)

# df1 = df
# # print(df1)

# df1['doj1'] = [
#     "12-04-2020",
#     "28-09-2021",
#     "05-02-2022",
#     "19-11-2023",
#     "23-03-2024",
#     "07-08-2025"
# ]

# df1['doj1'] = pd.to_datetime(df1['doj1'],format="%d-%m-%Y")
# print(df1.dtypes)

#extract Year,Month,day,week
# print(df['doj'].dt.year)
# print(df['doj'].dt.month)
# print(df['doj'].dt.day)
# print(df['doj'].dt.day_name())
 
df['pd'] = df['doj']+pd.Timedelta(days=90)
print(df['pd'])

df.drop('pd',axis=1,inplace=True)

df.to_csv('test_data.csv',index=False)