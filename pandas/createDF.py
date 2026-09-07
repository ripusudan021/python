import pandas as pd
df = pd.DataFrame([11,22,33],columns=['integer'])
print(df)

print(type(df))

data = {
    "name" : ["bob","alice","john","sam"],
    "age":[22,24,23,25],
    "city":["Jabalpur","bhopal","indore","nagpur"]
}

df = pd.DataFrame(data)
print(df)