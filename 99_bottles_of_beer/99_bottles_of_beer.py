def b(i):
	if i>1:
		s=f'{i} bottles'
	elif i==1:
		s=f'{i} bottle'
	else:
		s=f'no more bottles'
	return f'{s} of beer on the wall'
def c(i):
	if i>0:
		s=f'Take one down and pass it around, {b(i-1)}.\n'
	else:
		s=f'Go to the store and buy some more, {b(99)}.\n'
	return s
for i in range(99,-1,-1):
	print(b(i).capitalize()+f', {b(i)[:-12]}.\n{c(i)}')