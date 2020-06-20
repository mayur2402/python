import matplotlib.pyplot as plt

num = [1,2,3,4,5]
square = [1,4,9,16,25]

plt.plot(num,square, linewidth = 5)
plt.title("first graph",fontsize = 24)
plt.xlabel("value",fontsize = 15)
plt.ylabel("numbers",fontsize = 15)

plt.show()

