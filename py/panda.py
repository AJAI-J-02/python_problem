import pandas as pd

df=pd.read_csv("employee.csv")
print(df)
print(df.sort_values("name")["name"])

print(df.sort_values("salary",ascending=False)["name"])
print(df[["name","institution"]])
