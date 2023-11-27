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


# print(df)



#average price of an item
# sum of items
#sum of amount

#sum of amounts divided by sum of items


sum_items = df["Items"].sum()



sum_items = int(sum_items)

print(sum_items)


sum_amount = df["Amount"].sum()



sum_amount = int(sum_amount)


print(sum_amount)


avg_price_item = (sum_amount/sum_items)


print(avg_price_item)

#(avg price of item is 3.3709.....)




#average basket price

#sum of amounts divided by number of transactions


# count of transactions =

print(df)

print(df.shape)

# 30 rows, 5 columns

# 30 transactions

print(sum_amount/30)

# average basket price is 6.966666...




#maximum spend in one transaction

#.max of amounts


# print(df.max(axis = 1))

#make a new column of just amount

df2 = df["Amount"]

print(df2)

print(df2.max())

#max amount is 56.5




#minimum spend

#.min of df2

print(df2.min())

#min spend is 2.20




#most common spend amount

#the mode of amounts


print(df2.mode().loc[0])

#mode is 2.85




#most common payment type

# mode of currency type column

df3 = df["Currency"]

print(df3)

print(df3.mode())

#most common currency / payment type is Debit