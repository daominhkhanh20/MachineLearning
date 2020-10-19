from matplotlib import pyplot as plt 
import numpy as np 
from scipy.stats import norm

x_axis=np.arange(-3,3,0.001)

plt.plot(x_axis,norm.pdf(x_axis,0,0.5))

plt.plot(x_axis,norm.pdf(x_axis,0,1))

plt.savefig('kk.png')