strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ""

for i in strings:
	if i != 4:
		sentence = sentence + i + ' '
	else:
		sentence = sentence + i

print(sentence)
print(' '.join(strings))
