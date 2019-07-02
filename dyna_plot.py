import sys
import Adafruit_DHT
import datetime
import csv
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation

style.use('fivethirtyeight')

fig = plt.figure()
axl = fig.add_subplot(1,1,1)
xs = []
ys = []
print(x)
def animate(i):
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	print(str(temperature)+" temp")
	print(str(humidity)+" humidity")
	ys.append(temperature)
	xs.append(str(i))
	axl.clear()
	axl.plot(xs,ys)

while True:
	ani = animation.FuncAnimation(fig, animate, interval = 1000)
	plt.show()

