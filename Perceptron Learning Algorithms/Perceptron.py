import numpy as np 
from matplotlib import pyplot as plt 
#lib for save graph into file pdf
from matplotlib.backends.backend_pdf import PdfPages
def predict(w,X):
	return np.sign(X.dot(w))

def perceptron_algorithms(w_init,X,y):
	"""
	X is 2-d numpy aray with shape(N,d), each row is data point
	y is 1-d numpy array with shape(d,1), each element is label for data point
	w_init is 1-d numpy array with shape(d,1)
	"""
	w=w_init
	iteration=0
	while True:
		iteration+=1
		pre=predict(w,X)
		#find index for misclassified point
		mis_index=np.where(np.equal(pre,y)==False)[0]#convert to array
		number_misclassified=mis_index.shape[0]

		if number_misclassified==0:
			print(iteration)
			return w
		#np.rando.choice(array,number_datapoint_pick) return array
		random_index=np.random.choice(mis_index,1)[0]
		w+=y[random_index]*X[random_index]


	print(iteration)
	return w

if __name__=="__main__":

	#generate data for algorithms
	means=[[-1,0],[1,0]]
	covariance_matrix=[[0.3,0.2],[0.2,0.3]]
	#number data point in each domain
	n=50
	x1=np.random.multivariate_normal(means[0],covariance_matrix,n)
	x2=np.random.multivariate_normal(means[1],covariance_matrix,n)
	#each row is data point 
	X=np.concatenate((x1,x2),axis=0)
	#label for each domain,-1/1
	y=np.concatenate((np.ones(n),-1*np.ones(n)))
	#add 1 dimention into each data point (bias trick)
	Xbar=np.concatenate((np.ones((2*n,1)),X),axis=1)

	#generate for w
	w_initial=np.random.randn(Xbar.shape[1])
	w=perceptron_algorithms(w_initial,Xbar,y)
	#print normal vector for hyperplane
	print(w) 


	#save file into visulization1.pdf
	file_name="visuaization.pdf"
	with PdfPages(file_name) as pdf:
		#visualization for data point
		plt.plot(x1[:,0],x1[:,1],'bs')#blue square
		plt.plot(x2[:,0],x2[:,1],'ro')#red cicle marker
		plt.axis('equal')
		plt.xlabel('$x1$',fontsize=20)
		plt.ylabel('$x2$',fontsize=20)
		#draw the normal vector for hyperplane
		x_temp=np.arange(-1.5,1.5,0.1)
		c,a,b=w[0],w[1],w[2]
		y=-a/b*x_temp-c/b
		plt.plot(x_temp,y,'k')
		pdf.savefig(bbox_inches='tight')
		plt.show()


"""
NOTE:
 character	color
	'b'	    blue
	'g'	    green
	'r'	    red
	'c'	    cyan
	'm'	    magenta
	'y'	    yellow
	'k'	    black
	'w'	    white

"""