'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''
n = int(input("enter a number: "))

  
fiblist = []
i = 1

if n == 0:
	print(fiblist)
else: 
	while i < (n + 1):
		if i == 1:
			fiblist.append(i)
		elif i == 2:
			fiblist.append(1)
		else:
			a = fiblist.pop()
			b = fiblist.pop()
			fiblist.append(a)
			fiblist.append(b)
			fiblist.append(a+b)
		i += 1
	
	print(fiblist)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
