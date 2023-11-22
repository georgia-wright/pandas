import pandas as pd
import numpy as np


df = pd.read_excel("first_hour_sales.xlsx")




df = df.set_index("Transaction ID")


df = df.drop(columns = ["Till ID"])

df = df.drop("Staff ID", axis = 1)



df = df.drop([16,17,18])

# print(df)

df = df.drop_duplicates()

# print(df)


print(df["Amount"].mean())

print(df["Amount"].median())

print(df["Amount"].mode())

# print(df)

df.at[12,"Amount"] = 3.10



def float_to_time(stamp):
    stamp = str(stamp)
    stamp = stamp.replace(".", ":")
    stamp = "0" + stamp
    if len(stamp) != 5:
        stamp = stamp + "0"
    return stamp

df["Time"] = df["Time"].apply(float_to_time)


def extract_time(stamp):
    stamp = stamp.time()
    return stamp 


df["Time"] = pd.to_datetime(df["Time"])

df["Time"] = df["Time"].apply(extract_time)


print(df)



