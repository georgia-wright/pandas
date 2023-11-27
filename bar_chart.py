import matplotlib.pyplot as plt


advertising_locations =[
    "Twitter",
    "Facebook",
    "LinkedIn",
    "Indeed",
    "Instagram"
]

responses = [3,11,16,13,2]

bars = plt.bar(advertising_locations, responses)

bars[2].set_color('red')

plt.title("Return from Job Posting By Location")

plt.xlabel("Advert Location")

plt.ylabel("Applications Received")


plt.show()



