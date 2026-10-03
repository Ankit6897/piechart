import numpy as np
import matplotlib.pyplot as plt
# Total sixes scored by teams in ipl from 2026 in percentage.


sixes=np.array([12.69,11.99,11.50,11.43,9.82,8.91,8.7,8.7,8.2,8.06])
mylabels=["RR= 12.69%(highest)","SRH= 11.99%","RCB= 11.50%","PBKS= 11.43%","MI= 9.82%","LSG= 8.91%","GT= 8.7%","CSK= 8.7%","DC= 8.2%","KKR= 8.06%(lowest)"]

plt.pie(sixes,labels=mylabels)
mycolors=["#E91E63","orange","#E91E1E","red","blue","#0057E2","#F8B6C1","yellow","lightblue","purple"]
plt.pie(sixes, labels=mylabels, colors=mycolors)
plt.suptitle("Total sixes scored by teams in ipl from 2026 in percentage The total sixes=1,426",color="purple")
plt.show()