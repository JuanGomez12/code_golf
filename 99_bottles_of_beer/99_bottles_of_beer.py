def b(i):
	if i>1:
		return f"{i} bottles"
	elif i==1:
		return f"{i} bottle"
	else:
		return 'no more bottles'

def c(i):
	if i>0:
		s=f'Take one down and pass it around, {b(i-1)} of beer on the wall.\n'
	else:
		s=f'Go to the store and buy some more, 99 bottles of beer on the wall.\n'
	return s
for i in range(99,-1,-1):
	print(b(i).capitalize()+f' of beer on the wall, {b(i)} of beer.\n{c(i)}')