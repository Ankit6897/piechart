import numpy as np
import matplotlib.pyplot as plt
# Total wickets taken by teams in ipl from 2026 in percentage.
wickets = np.array([
    14.73, 12.57, 12.57, 11.38, 10.42,
    9.82, 8.98, 8.38, 8.02, 3.11
])

mylabels = [
    "GT = 14.73%(highest)",
    "RCB = 12.57%",
    "RR = 12.57%",
    "SRH = 11.38%",
    "KKR = 10.42%",
    "CSK = 9.82%",
    "MI = 8.98%",
    "DC = 8.38%",
    "PBKS = 8.02%",
    "LSG = 3.11%(lowest)"

]
plt.pie(wickets,labels =mylabels)
mycolors = [
    "#E91E63", "orange", "#E91E1E", "red", "blue",
    "#0057E2", "#F8B6C1", "yellow", "lightblue", "purple"
]
plt.pie(wickets, labels=mylabels, colors=mycolors)
plt.suptitle("Total wickets taken by each team in ipl 2026,The total wickets=835", color="purple")
plt.show()
