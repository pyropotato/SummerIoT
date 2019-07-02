#plotting from file
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv

style.use('fivethirtyeight')

fig = plt.figure()
axl = fig.add_subplot(1,1,1)
xs = []
ys = []
def animate(i):
    x = 0
    with open('reading.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')
        for row in plots:
            xs.append(str(x))
            ys.append(row[0])
            x+=1

    axl.clear()
    axl.plot(xs,ys)
    axl.plot(xs,ys)

while True:
    ani = animation.FuncAnimation(fig, animate, interval = 1000)
    plt.show()
