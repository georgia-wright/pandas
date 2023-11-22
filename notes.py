import pandas as pd
import numpy as np

languages = pd.Series(['Python', 'JavaScript', 'HTML', 'SQL'])

print(languages)

ranking = pd.Series([3, 1, 2, 4])

print(ranking)

#create a data frame using the kwarg format

# df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie", 55)], columns = ["Name", "Age"])


# print(df)

# create a data frame using the dictionary format:

df = pd.DataFrame ({
    "Languages" : languages,
    "Ranking" : ranking
})

# print(df)

# --------------------------------------------

# ammending data structures

# ---------------------------------------------

df.loc[4] = ["PHP", 11]

# print(df)

df.loc[5] = ["Java", 7]
df.loc[6] = ["TypeScript", 5]

# print(df)


# add data as a column

df["Ranking 2022"] = [4,1,2,3,10,6,5]

# print(df)

df["Ranking 2020"] = [4,1,2,3,8,5,9]

df["Ranking 2019"] = [4,1,2,3,8,5,10]

# print(df)

df.insert(3, "Ranking 2021", [3,1,2,4,11,5,7])


# print(df)

# print(df.shape)

# print(df.columns)

# print(df[["Ranking 2019", "Ranking 2022"]])

# print(df)

# print(df.loc[0:3:1, "Languages": "Ranking 2020": 2])

# print(df[df<4])


# print(df[df.select])



#______________________

#Small data cleaning

#_______________________

# print(df)

df.rename(columns = {"Ranking" : "Ranking 2023"}, inplace=True)

# print(df)

df.set_index("Languages", inplace=True)

# print(df)

# print(df["Ranking 2019"])


# print(df.loc["HTML"])

print(df.mean(axis=1))

# print(df)

print(df.mode(axis=1))

print(df.median(axis=1))

print(df.min(axis=1))

print(df.max(axis=1))

print(df.sort_values(by=["Ranking 2022"], ascending=False))










