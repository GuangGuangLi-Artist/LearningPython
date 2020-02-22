from matplotlib import pyplot as plt


x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

fig = plt.figure(figsize=(32,20),dpi=100)

plt.plot(x,y)

#设置x轴的刻度
_xtickets = [i/2 for i in range(4,49)]
plt.xticks(_xtickets[::2])
plt.yticks(range(min(y),max(y)+1))

# plt.xticks(range(20,50))
plt.savefig("./save_fig.png")

plt.show()