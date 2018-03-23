from os import system
from itertools import count
from math import sin,cos,acos
import random

clear = lambda: system('cls')

class Vector(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.mag = (x**2 + y**2) ** 0.5
	def neg(self):
		return(Vector(-self.x, -self.y))
	def add(self, v2):
		return(Vector(self.x+v2.x, self.y+v2.y))
	def sub(self, v2):
		return(self.add(v2.neg()))
	def mul(self, c):
		return(Vector(c*self.x, c*self.y))
	def rot(self, theta):
		alpha = acos(self.x / self.mag)
		beta = alpha + theta
		return(Vector(self.mag*cos(beta), self.mag*sin(beta)))
		
def genPrimes():
	D = {}
	for q in count(2):
		p = D.pop(q, None)
		if p is None:
			yield q
			D[q*q] = q
		else:
			x = p + q
			while x in D:
				x += p
			D[x] = p

def primesbelow(N):
	correction = N % 6 > 1
	N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
	sieve = [True] * (N // 3)
	sieve[0] = False
	for i in range(int(N ** .5) // 3 + 1):
		if sieve[i]:
			k = (3 * i + 1) | 1
			sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
			sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
	return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]

def isprime(n, precision=7):
	_smallprimeset = 10**5
	smallprimeset = set(primesbelow(_smallprimeset))
	if n == 1 or n % 2 == 0:
		return False
	elif n < 1:
		raise ValueError("Out of bounds, first argument must be > 0")
	elif n < _smallprimeset:
		return n in smallprimeset

	d = n - 1
	s = 0
	while d % 2 == 0:
		d //= 2
		s += 1

	for repeat in range(precision):
		a = random.randrange(2, n - 2)
		x = pow(a, d, n)

		if x == 1 or x == n - 1: continue

		for r in range(s - 1):
			x = pow(x, 2, n)
			if x == 1: return False
			if x == n - 1: break
		else: return False

	return True

def pollard_brent(n):
	if n % 2 == 0: return 2
	if n % 3 == 0: return 3

	y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
	g, r, q = 1, 1, 1
	while g == 1:
		x = y
		for i in range(r):
			y = (pow(y, 2, n) + c) % n

		k = 0
		while k < r and g==1:
			ys = y
			for i in range(min(m, r-k)):
				y = (pow(y, 2, n) + c) % n
				q = q * abs(x-y) % n
			g = gcd(q, n)
			k += m
		r *= 2
	if g == n:
		while True:
			ys = (pow(ys, 2, n) + c) % n
			g = gcd(abs(x - ys), n)
			if g > 1:
				break

	return g

def primefactors(n, sort=False):
	factors = []
	smallprimes = primesbelow(1000)
	limit = int(n ** .5) + 1
	for checker in smallprimes:
		if checker > limit: break
		while n % checker == 0:
			factors.append(checker)
			n //= checker
			limit = int(n ** .5) + 1
			if checker > limit: break

	if n < 2: return factors

	while n > 1:
		if isprime(n):
			factors.append(n)
			break
		factor = pollard_brent(n)
		factors.extend(primefactors(factor))
		n //= factor

	if sort: factors.sort()

	return factors

def factorization(n):
	factors = {}
	for p1 in primefactors(n):
		try:
			factors[p1] += 1
		except KeyError:
			factors[p1] = 1
	return factors

def totient(n):
	totients = {}
	if n == 0: return 1

	try: return totients[n]
	except KeyError: pass

	tot = 1
	for p, exp in factorization(n).items():
		tot *= (p - 1)  *  p ** (exp - 1)

	totients[n] = tot
	return tot

def gcd_steps(a, b):
	c = 0
	if a == b: return a
	while b > 0: 
		a, b = b, a % b
		c += 1
	return c

def gcd(a, b):
	if a == b: return a
	while b > 0: a, b = b, a % b
	return a

def lcm(a, b):
	return abs(a * b) // gcd(a, b)