w=' on the wall'
f=' bottles of beer'
def b(i):
	if i>1:
		s=f'{i}{f}'
	elif i==1:
		s=f'{i} bottle of beer'
	else:
		s=f'no more{f}'
	return s
def c(i):
	if i>0:
		s=f'Take one down and pass it around, {b(i-1)}{w}.\n'
	else:
		s=f'Go to the store and buy some more, 99{f}{w}.\n'
	return s
for i in range(99,-1,-1):
	print(b(i).capitalize()+f'{w}, {b(i)}.\n{c(i)}')