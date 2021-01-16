# your code goes here

import random
import numpy as np
# n -> m
def init():
	global n,m
	n = 3
	m = 4
def f(x):
	return [0] + x

def GetF(k, f):
	def F(x):
		ret = []
		for i in range(0,k):
			ret = ret + f(list(x[i]))
		return ret
	return F
def getk(epsilon):
	global n
	return 2*n/epsilon
# take mk and output nk 
def A(x):
	global m, n 
	nx = len(x)
	ret = []
	r = []
	for i in range(0,nx):
		if i > 0 and i % m == 0:
			ret.append(r) 
			r = []
		if i % m == 0:
			continue
		r.append(x[i])
	ret.append(r)
	return ret


# y : {0,1}^m
def B(k, delta, y):
	global m, n
	F = GetF(k,f)
	for i in range(0, int((k**2) * n/ delta)):
		x  = np.random.randint(2, size=n * k)
		x = x.reshape((k,n))
		y_bar= F(x)
		y[i] = y_bar[i]
		x_prime = np.asarray(A(y)).reshape((k,n))
		if F(x_prime) == y:
			return x_prime
		
	
	print("failed")


init()

print(B(2, 1, [0,0,0,0,0,0,0,0]))
