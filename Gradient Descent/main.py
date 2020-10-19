from numpy import sin,cos
import numpy as np 
from matplotlib import pyplot
def gradient(x):
	return 2*x+5*cos(x)

def cost(x):
	return x**2+5*sin(x)

def gradient_algo(x0,learning_rate):
	x=[x0]

	for i in range(10000):
		x_new=x[-1]-learning_rate*gradient(x[-1])
		if abs(gradient(x_new)) <1e-4:
			break

		x.append(x_new)

	return (x,i)


if __name__=="__main__":

	(x1,iterations1)=gradient_algo(5,0.1)
	y1=[cost(i) for i in x1]
	(x2,iterations2)=gradient_algo(-5,0.1)
	y2=[cost(i) for i in x2]

    #draw graph
	x=np.linspace(-10,10,1000)
	y=x**2+5*sin(x)
	pyplot.plot(x,y,'y')
	pyplot.plot(x1,y1,'.','r')
	pyplot.plot(x2,y2,'.','b')
	pyplot.show()

    #find global minimum for solution
	print("Solution for x1=%0.5f Cost=%0.5f  Iteration=%d"%(x1[-1],cost(x1[-1]),iterations1))
	print("Solution for x2=%0.5f Cost=%0.5f  Iteration=%d"%(x2[-1],cost(x2[-1]),iterations2))