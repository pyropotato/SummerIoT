import matplotlib.pyplot as plt
import numpy as np
slices = [7,2,2,13]
activities = ['A','B','C','D']
cols =['c','m','r','b']
np.random.seed(123123123)
mu, sigma = 100,15
x = mu + sigma * np.random.randn(10000)
plt.subplot(221)
plt.bar(activities,slices)
plt.subplot(222)
plt.pie(slices,labels = activities,colors = cols, startangle = 90,shadow = False,explode =(0,0.1,0,0),autopct = '%1.1f%%')
plt.title("Title")
plt.legend()
plt.subplot(223)
plt.hist(x, 50, normed=1, facecolor='g',alpha=0.75)
plt.xlabel('data',fontsize = 14,color = 'red')
plt.ylabel('Probability')
plt.title(r'$\sigma_i=15$')
plt.text(60,0.025,r'$\sigma_mu=100,\ \sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.subplot(224)
plt.plot([1,2,3,4,5,6,10,20,13,5,2,1],'ro')
plt.show()
