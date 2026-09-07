import pandas as pd
data = {
    "name" : ["bob","alice","john","sam"],
    "age":[22,24,23,25],
    "city":["Jabalpur","bhopal","indore","nagpur"]
}

df = pd.DataFrame(data)
print(df)

#Return Top 5 entries
print(df.head(2)) # head(n) : where is the number of rows


#Return Bottom 5 entries
print(df.tail(2)) # tail(n) : where is the number of rows

print(df.shape)
print(df.columns)

print(df.rename(columns={"city":"COB"}),)
print(df.info())

print(df.describe())
