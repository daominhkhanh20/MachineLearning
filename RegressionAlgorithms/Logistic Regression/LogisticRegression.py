import numpy as np 
from math import exp
from matplotlib import pyplot as plt

def sigmoid_function(s):
	return 1/(1+exp(-s))

def loss_function(w,X,y,lamda):
	n=X.shape[0]
	z=[sigmoid_function(np.dot(w,X[i].T))  for i in range(n)]
	s1=-1/n*sum(y[i]*np.log(z[i])+(1-y[i])*np.log(1-z[i]) for i in range(n))
	s2=0.5*lamda*np.sum(w*w)/n
	return s1+s2


#using stochastic gradient desent
def logistic_algorithms(X,y,lamda,w_init,learn_rate,epochs):
	n,d=X.shape[0],X.shape[1]
	w=[w_init]
	loss_value=list()
	loss_value.append(loss_function(w[-1],X,y,lamda))
	for i in range(epochs):
		random_index_in_range_n=np.random.permutation(n)
		for i in random_index_in_range_n:
			xi=X[i]
			yi=y[i]
			sigmoid=sigmoid_function(np.dot(w[-1],xi.T))
			w_new=w[-1]-learn_rate*((sigmoid-yi)*xi+lamda*w[-1])
			if np.linalg.norm(w_new-w[-1])/d<1e-6:
				return (w,loss_value)
			loss_value.append(loss_function(w_new,X,y,lamda))
			w.append(w_new)
			
	return (w,loss_value)

if __name__=="__main__":
	np.random.seed(1)
	X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,
				2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]])
	y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])
	n=X.shape[1]
	Xbar=np.concatenate((X.T,np.ones((n,1))),axis=1)
	lamda=0.0001
	w_init=np.random.randn(Xbar.shape[1])
	(w,loss_value)=logistic_algorithms(Xbar,y,lamda,w_init,0.05,epochs=500)
	print(w[-1])
	fig,(axs1,axs2)=plt.subplots(1,2)

	#visualization 
	y0=y[np.where(y==0)[0]]
	x0=X[0,np.where(y==0)][0]
	y1=y[np.where(y==1)[0]]
	x1=X[0,np.where(y==1)][0]
	axs1.plot(x0,y0,'ro',markersize=6)
	axs1.plot(x1,y1,'bs',markersize=6)
	axs1.set_xlabel("Hours")
	axs1.set_ylabel("Pass or no")

	xx=np.linspace(-1,6,1000)
	w1,w0=w[-1][0],w[-1][1]
	#threshold=-w0/w1
	#plt.plot(threshold, .5, 'y^', markersize = 8)
	yy=[sigmoid_function(w0+w1*i) for i in xx]
	axs1.plot(xx,yy,'g-',linewidth=2)

	size_loss_value_list=len(loss_value)
	iterations=np.linspace(1,size_loss_value_list,size_loss_value_list).astype(int)
	axs2.plot(iterations,loss_value)
	axs2.set_xlabel("iterations")
	axs2.set_ylabel("Loss value")
	fig.tight_layout(pad=3.0)
	plt.savefig("viusalization.png")







