import matplotlib.pyplot as plt
from datetime import datetime

graph_data = open('C:\\Users\\acer\\Documents\\School 2\\App Dev\\LESSONS AND EXCER\\EXCER3\\python\\graph\\examples.txt', 'r').read()
lines = graph_data.split('\n')

xs = []
ys = []

for line in lines:
       if len(line) > 1:
              x, y = line.split(', ')
              xs.append(float(x))
              ys.append(float(y))

fig = plt.figure()
date = datetime.now()
date = date.strftime("%Y/%m/%d %H:%M:%S")
axl = fig.add_subplot(1,1,1)
axl.clear()

axl.plot(xs, ys, 'b--', label='abc')

plt.title("TITLE OF DA GRAPH")
plt.ylabel("Celcius", fontweight='bold')
plt.xlabel(f"{date}", fontweight='bold')
plt.axis([0,60,0,100])
plt.axhspan(27,35, facecolor="green", alpha = .5) #alpha is transparency
plt.axhspan(35,41, facecolor="yellow", alpha = 0.5)
plt.axhspan(41,55, facecolor="orange", alpha = 0.5)
plt.axhspan(55,100, facecolor="pink", alpha = 0.5)


plt.legend()
plt.savefig('yey.png')
plt.show()
