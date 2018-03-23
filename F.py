from sean import factorization
from time import clock

st = clock()

def F(n, offset=1):
	fin = factorization(n)
	out = offset
	for prime in fin:
		out += prime * fin[prime]
	return(out)

def kmax(d):
	v = list(d.values())
	k = list(d.keys())
	return k[v.index(max(v))]

	
limit = 10**6
fixedpoint = (7,8)
count = {k: 0 for k in range(7, limit+1)}
km = 0

for i in range(9, limit+1):
	if count[i] > 0:
		continue
	j = 1
	c = F(i)
	chain = [i]
	if c not in fixedpoint and count[c] == 0:
		chain.append(c)
		c = F(c)
		j += 1
	for k in chain:
		if count[k] > 0:
			break
		count[k] = j + count[c]
		if count[k] > km:
			print(k, count[k])
			km = count[k]
		j -= 1

k = kmax(count)
ck = count[k]

print(k, ck, clock()-st)

j = 0
while j < ck:
	print(k)
	k = F(k)
	j += 1