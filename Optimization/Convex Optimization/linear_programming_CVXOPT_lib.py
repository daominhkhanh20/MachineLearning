from cvxopt import solvers, matrix
"""
 (x,y)=arg max(5x+3y)

 Condition: x+y<=10
            2x+y<=16
            x+4y<=32
            x,y>=0

Solution:
convert condition into
			x+y<=10
            2x+y<=16
            x+4y<=32
            -x<=0
            -y<=0

			           1 1                  10
==>			matrix(G)= 2 1       matrix(d)= 16
			           1 4                  32
			           -1 0                  0
			           0 -1                  0
G*[x y].T<=d


"""
c = matrix([-5., -3.])
G = matrix([[1., 2., 1., -1., 0], [1., 1., 4., 0., -1.]])
d = matrix([10., 16., 32., 0., 0.])
sol = solvers.lp(c, G, d)
print(sol)
print(sol['x'])
