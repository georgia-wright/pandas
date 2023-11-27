import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022, 2023]

python_position = [7, 4, 4, 3, 4, 3]

javascript_position = [1, 1, 1, 1, 1, 1]

sql_position = [4, 3, 3, 4, 3, 4]

typescript_position = [12, 10, 9, 7, 5, 5]

plt.plot(years, python_position, label = "Python")

plt.plot(years, javascript_position, label = "JavaScript", linestyle = "dashed")

plt.plot(years, sql_position, label = "SQL", linestyle = "dotted")

plt.plot(years, typescript_position, label = "Typescript", linestyle = "dashdot")


plt.title("Most Popular Language Ranking")




plt.xlabel("Year")

plt.ylabel("Position")


plt.ylim(bottom=10, top=0)

plt.legend()

plt.show()