import random
deck = [i for i in range(52)]
random.shuffle(deck)
print(deck)
numstacks = 7
stack = [[]] * numstacks

# 0 - 0
# 1 - 1,2
# 2 - 3,4,5
# 3 - 6,7,8,9
# 4 - 10,11,12,13,14
# 5 - 15,16,17,18,19,20
# 6 - 21,22,23,24,25,26,27
# d - 28, ..., 51

cs = 0
c = 1
lim = int(numstacks * (numstacks + 1) * (1/2))

for i in range(numstacks):
	for j in range(c):
		
	c += 1