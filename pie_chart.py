import matplotlib.pyplot as plt

roles = [    
    "Front-end", 
    "Back-end",
    "Full-stack",
    "DevOps"
    ]

employees = [52,36,28,11]

plt.pie(employees, labels=roles, autopct="%.2f%%", explode = [0.2,0,0,0])

plt.title("Developer Roles")

plt.savefig("pie.png")

plt.show()

