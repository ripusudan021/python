import pandas as pd

data = {
    "name" : ["bob","alice","john","sam"],
    "age":[22,24,23,25],
    "city":["Jabalpur","bhopal","indore","nagpur"]
}

# df = pd.DataFrame(data)
# print(df)

# #save and load as/from CSV

# df.to_csv('test_Data.csv',index=False)

load_df = pd.read_csv('test_Data.csv')
print(load_df)