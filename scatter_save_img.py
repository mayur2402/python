import matplotlib.pyplot as plt

x = [1,2,3,4,5]

y = [1,4,9,16,25]

plt.scatter(x,y,c=y,cmap = plt.cm.Blues, s = 100,edgecolor = 'red')

plt.plot(x,y)

plt.title("Scatter point", fontsize = 20)
plt.xlabel("X-axis value", fontsize = 10)
plt.ylabel("y-axis value", fontsize = 10)
plt.tick_params(axis = 'both', which = 'major')

plt.savefig('scatter.png',bbox_inches = 'tight')
