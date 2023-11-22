import pandas as pd
import numpy as np


time = pd.Series(['00:00', 'O0:30', '01:00', '01:30', '02:00', '02:30', "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00"])

download_speed = pd.Series([203.22, 192.34, 202.63, 178.32, 166.29, 145.61, 180.62, 184.10, 158.31, 179.96, 179.79, 168.88, 134.24, 185.56, 191.94, 177.43, 161.32, 189.86, 218.59, 93.33, 188.99])


upload_speed = pd.Series([83.24, 74.78, 43.28, 65.96, 58.34, 60.83, 30.96, 56.88, 30.74, 62.02, 60.12, 61.92, 72.41, 79.25, 57.59, 83.14, 86.31, 30.84, 86.54, 84.57, 74.64])

idle_latency = pd.Series([11, 7, 11, 18, 30, 32, 10, 12, 16, 6, 11, 4, 11, 4, 6, 11, 5, 4, 17, 6, 10])

df = pd.DataFrame ({
    "Time" : time,
    "Download Speed" : download_speed,
    "Upload Speed" : upload_speed,
    "Idle Latency" : idle_latency

})



df = df.set_index("Time")

# print(df)



ds_mean = df["Download Speed"].mean()

ds_mean = f"{ds_mean:.2f}"

us_mean = df["Upload Speed"].mean()

us_mean = f"{us_mean:.2f}"

print(us_mean)

il_mean = df["Idle Latency"].mean()


il_mean = f"{il_mean:.2f}"

print(il_mean)


# df.loc[21] = [ds_mean, us_mean, il_mean]

print(df)

ds_mode = df["Download Speed"].mode()

print(ds_mode)

us_mode = df["Upload Speed"].mode()

print(us_mode)

il_mode = df["Idle Latency"].mode()

# print(il_mode)


# df.loc[22] = [ds_mode, us_mode, il_mode]




# #median

# ds_median = df["Download Speed"].median()

# print(ds_median)

# us_median = df["Upload Speed"].median()

# print(us_median)

# il_median = df["Idle Latency"].median()

# print(il_median)


# df.loc[23] = [ds_median, us_median, il_median]





# SORTING:

# print(df.sort_values(by=["Download Speed"], ascending=False))

# print(df.sort_values(by=["Upload Speed"], ascending=True))























