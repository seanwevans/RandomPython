from itertools import combinations
from sean import primes, isprime

def D(n):
	if isprime(n):
		return(1)
	else:
		pass

k = 1
small_primes = sean.primes(100)
a = {}
for i in range(1,4):
	for j in combinations(small_primes, i):
		pr = 1
		for k in i:
			pr *= k
		a[k] = D(k)