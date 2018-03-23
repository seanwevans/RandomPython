import random
import itertools

ranks = [t for t in range(13)]
deck = ranks * 4
random.shuffle(deck)
player1 = deck[:26]
player2 = deck[26:]
c=0
while(player1 != [] and player2 != []):
	#c+=1
	#print(c)
	print(len(player1), len(player2))
	if player1[0] >= player2[0]:
		player1.append(player1[0])
		player1.append(player2[0])
		del player1[0]
		del player2[0]
		#print("Player1")
		continue
	if player2[0] > player1[0]:
		player2.append(player1[0])
		player2.append(player2[0])
		del player1[0]
		del player2[0]
		#print("player2")
	#print(player1[0],player2[0],len(player1),len(player2))
		
