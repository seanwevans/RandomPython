def check(word, magic=219):	
	for i in range(len(word) // 2):		
		if (ord(word[i]) + ord(word[-i-1]) != magic):				
		#if word[i] != word[-i-1]:									# palindromes
			return False
	return True		
		
def form(word):
	wo = ''
	for letter in word.rstrip():
		if (ord(letter) >= ord('a')):
			wo += letter.lower()
	return wo

def transform(word):
	b = []
	for i in range(len(word) // 2):
		b.append(ord(word[i]) + ord(word[-i-1]))
	return b

def allsame(nums):	
	s = nums[0]
	for n in nums:
		if n != s:
			return False
	return True

if __name__ == "__main__":
	from sys import argv
	
	dictionary = open('dict1689k.txt', 'r')
	ans = {i:[] for i in range(ord('a')*2,ord('z')*2+1)}

	for word in dictionary:
		test = form(word)
		transtest = transform(test)
		if(len(test) >= 6 and allsame(transtest) and test not in ans[transtest[0]]):
			#ans.append((test,transtest[0]))
			ans[transtest[0]].append(test)
	#ans.sort()
	
	for key in ans:
		ans[key].sort()
		print(key-192, len(ans[key]), ans[key])
	
	dictionary.close()
	
	


	#for word in dictionary:	
	#	test = form(word)	
	#	if (len(test) >= 2 and test not in ans and check(test)):
	#		ans.append(test)
	#ans.sort()
	#print(ans)
	#print(len(ans))