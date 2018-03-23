def wizardQ(word):
	mv = ord('a') + ord('z')
	for i in range(len(word)//2):
		if (ord(word[i]) + ord(word[-1-i]) != mv):
			return(False)
	return(True)

def palindromeQ(word):
	for i in range(len(word)//2):
		if word[i] != word[-1-i]:
			return(False)
	return(True)
	
def constantWidthQ(word):
	for i in range(len(word)-2):
		a = ord(word[i])
		b = ord(word[i+1])
		c = ord(word[i+2])
		if abs(b-a) != abs(c-b):
			return(False)
	return(True)

def countConsecutiveLetters(word):
	d = {}
	for i in range(len(word)-1):
		if word[i] == word[i+1]:
			wi = word[i] + word[i]
			if wi not in d.keys(): 	
				d[wi] = 0
			d[wi] += 1
	return(d)

def wordIsMadeFrom(word, madefrom):
	for c in word:
		if c not in madefrom:
			return(False)
	return(True)
	
def wordIsMadeWithout(word, madewithout):
	for c in word:
		if c in madewithout:
			return(False)
	return(True)
	
if __name__ == "__main__":
	from time import clock
	from random import sample
	from pprint import pprint
	
	start = clock()
	d = {}
	path = 'dict675k.txt'
	primes = [2,3,5,7,11,13,17,19,23]
	alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
	vowels = ['a','e','i','o','u','y']
	toprow = ['q','w','e','r','t','y','u','i','o','p']
	midrow = ['a','s','d','f','g','h','j','k','l']
	botrow = ['z','x','c','v','b','n','m']
	lefthand = toprow[:5] + midrow[:5] + botrow[:5]
	righthand = toprow[-5:] + midrow[-4:] + botrow[-2:]
	uniformRandomLetters = sample(alphabet, 7)
		
	with open(path, 'r') as wordlist:
	
		for word in wordlist:
			w = word.rstrip().lower()
			lenw = len(w)
			if lenw > 3 and "'" not in w:				
				#if wordIsMadeFrom(w, alphabet[:10]):				# words with just A-J
				#if wordIsMadeWithout(w, alphabet[:10]):			# words without A-J
				#if wordIsMadeFrom(w, vowels):						# words with all vowels
				#if wordIsMadeWithout(w, vowels):					# words with all consonants
				#if palindromeQ(w):									# palindromes
				#if wizardQ(w):										# "wizard" words
				#if constantWidthQ(w):								# words of constant width
				#if sum(countConsecutiveLetters(w).values()) > 2:	# words with more than 2 sets of consecutive letters				
				#if wordIsMadeFrom(w, toprow):						# words formed from just the top row of the keyboard
				#if wordIsMadeFrom(w, midrow)						# just the middle row of the keyboard
				#if wordIsMadeFrom(w, botrow):						# just the bottom row of the keyboard
				#if wordIsMadeFrom(w, lefthand):					# just the left hand
				#if wordIsMadeFrom(w, righthand):					# just the right hand
				#if 's' in w and w.count('s') > 7:					# words with more than 7 s's
				#if 'e' in w and w.count('e') > 5:					# words with more than 5 e's
				#if 'a' in w and w.count('a') > 5:					# words with more than 5 a's
				#if 'n' in w and w.count('n') > 5:					# words with more than 5 n's
				#if wordIsMadeFrom(w, alphabet[::2]):				# words formed from letters in the odd positions
				#if wordIsMadeFrom(w, alphabet[1::2]):				# words formed from even positional letters
				#if wordIsMadeFrom(w, uniformRandomLetters):		# words made from random letters
				if wordIsMadeWithout(w,midrow) and wordIsMadeFrom(w,lefthand):
					if lenw not in d.keys():	d[lenw] = []
					if w not in d[lenw]:		d[lenw].append(w)
	
	pprint(d)
	print(uniformRandomLetters, clock()-start)