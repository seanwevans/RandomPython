from random import randint
from sys import argv
for j in range(int(argv[2])):
	a=''
	for i in range(int(argv[1])):
		r=randint(33,126)
		a+=chr(r)
	print(a)