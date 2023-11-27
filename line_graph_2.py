import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

youtube = [2, 1, 3, 6, 3]

twitter = [1, 1, 0, 0, 2]

whatsapp = [3, 1, 0, 2, 1]

raid = [0, 4, 2, 3, 3]

tiktok = [3, 0, 1, 0, 2]

font1 = {'family':'serif','color':'CornflowerBlue','size':20}
font2 = {'family':'serif','color':'hotpink','size':15}

plt.plot(days, youtube, label = "YouTube", c = "BlueViolet", marker = '*')

plt.plot(days, twitter, label = "Twitter", linestyle = "dashed", c = "Aquamarine", marker = 'x')

plt.plot(days, whatsapp, label = "WhatsApp", linestyle = "dotted", c = "CornflowerBlue", marker = 'd')

plt.plot(days, raid, label = "Raid:Shadow Legends", linestyle = "dashdot", c = "Coral", marker = 'H' )

plt.plot(days, tiktok, label = "TikTok", c = "Crimson", lw = 2.5, marker = 'o')

plt.title("Screen Time on Websites", fontdict = font1)

plt.xlabel("Days", fontdict = font2)

plt.ylabel("Hours", fontdict = font2)

plt.legend()

plt.show()







# plt.plot(years, python_position, label = "Python")



