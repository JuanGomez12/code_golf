d='bottles'
e=' of beer'
w=' on the wall'
def b(i):
	if i>1:
		return f"{i} {d}"
	elif i==1:
		return f"{i} bottle"
	else:
		return f'no more {d}'
def c(i):
	if i>0:
		s=f'Take one down and pass it around, {b(i-1)}{e}{w}.\n'
	else:
		s=f'Go to the store and buy some more, 99 {d}{e}{w}.\n'
	return s
for i in range(99,-1,-1):
	print(b(i).capitalize()+f'{e}{w}, {b(i)}{e}.\n{c(i)}')