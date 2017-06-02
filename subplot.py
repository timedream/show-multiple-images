import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
fig = plt.figure()
a=fig.add_subplot(1,1,1)
data=np.loadtxt('dataim')
plt.plot(data[:,0],data[:,2])
b=fig.add_subplot(1,2,2)
plt.plot(data[:,1],data[:,2])
plt.show()
