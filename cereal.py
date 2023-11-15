import pandas as pd
import numpy as np

df = pd.read_csv("cereal.csv")

# print(df)

print(df.shape)

rows_columns = df.shape

# print(rows_columns[0])

# print(rows_columns[1])

print(f"There are {rows_columns[0]} rows and {rows_columns[1]} columns in this data frame.")


# print(df.columns)

print("The names of the columns are:")
for i in df.columns:
    print(i)


# print(df.loc[:, "protein"])


# print(df)

protein_df = df.loc[:, "name":"protein" : 4]

for i in protein_df:
    if protein_df[protein_df.select_dtypes (include= "int") > 4]:
        print(i)
    else:
        print()

        














