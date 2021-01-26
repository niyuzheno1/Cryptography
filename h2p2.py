# your code goes here
import random as r
def init():
	global n
	n = 1

def E(m):
	global n
	a = []
	for i in range(0,9):
		a = a+m
	return a

def D(m):
	return [m[0]]

def G(x):
	global n
	a = []
	for i in range(0,10):
		a = a + x
	return a

def distance(m0, m1):
	global n
	x = 0
	m0 = E(m0)
	m1 = E(m1)
	for i in range(0,9*n):
		if m0[i] != m1[i]:
			x = x+1
	return x

def getall():
	global n
	m = 10 * n
	a = []
	for i in range(0, 1<<m):
		cnt = 0
		for j in range(0,m):
			if (i & (1<<j)) > 0:
				cnt = cnt + 1
		if cnt == 9*n:
			a.append(i)
	return a
def tolists(x, l):
	a =[]
	for i in range(0, l):
		if (x & (1<<i)) > 0:
			a.append(1)
		else:
			a.append(0)
	return a
def pick(n):
	return r.randint(0, (1<<n)-1)
init()	
print(tolists(511,10))

def xor_list(a,b):
	n = len(a)
	c = [0]*n
	for i in range(n):
		c[i] = a[i]^b[i]
	return c

def game(m):
	global n
	R = r.choice(getall()) # B part
	R = tolists(R, 10*n)
	
	x = pick(n)
	x = tolists(x,n)
	
	gx = G(x)
	em = E(m)
	zn = tolists(0,n)
	
	pem = 0
	pzn = 0
	
	c = tolists(0, 10*n)
	for i in range(0, 10*n):
		if R[i] == 1:
			c[i] = em[pem]
			pem = pem + 1
		else:
			c[i] = zn[pzn]
			pzn = pzn + 1
	
	gxc = xor_list(gx, c)
			
	return R, x, gxc, c # last one for fault tolerance

def decommit(R, x, gxc):
	gx = G(x)
	c = xor_list(gxc, gx)
	em = []
	for i in range(0, 10*n):
		if R[i] == 1:
			em.append(c[i])
	return D(em)
	


R, x, gxc, c = game([1])
print(xor_list(G([0]), gxc) )
print(xor_list(G([1]), gxc) )
print(R)

