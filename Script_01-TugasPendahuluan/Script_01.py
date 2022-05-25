#Script 01: Pendahuluan
import numpy as np
import matplotlib.pyplot as plt

f = open('C:/Users/Daenk Himawa/Documents/Python Scripts/Tugas Semester 4/P-Tugas Pendahuluan Prak Pemos.txt', 'r')
data = np.genfromtxt(f, dtype="float", delimiter='\t',
names=True)
f.close()

depth = data['depth']
temp = data['temp']
sal = data['sal']
del(data)

mins = np.floor(np.min(sal))
maxs = np.ceil(np.max(sal))

fig1, (ax1, ax2) = plt.subplots(1,2,sharey=True,figsize=(9, 6))
ax1.plot(temp,depth,'o--b')
ax1.set_ylim(ax1.get_ylim()[::-1])
ax1.set_xlabel('Temperature [$^\circ$C]') 
ax1.set_ylabel('Depth (m)') 
ax1.xaxis.set_label_position('top') 
ax1.xaxis.set_ticks_position('top') 

ax2.plot(sal,depth,'o--r')
ax2.set_xlabel('Salinity')
ax2.set_xlim(mins,maxs)
ax2.xaxis.set_label_position('top')
ax2.xaxis.set_ticks_position('top')
ax2.yaxis.set_visible(False) 

plt.tight_layout()
plt.show()
fig1.savefig('Tugas Pendahuluan.jpg', dpi=300,  transparent=False)
