for i in range(3,10):
	for j in range(1,i+1):
		print(' '*(i-j+1)+'*'*(2*j-1))
	print(' '*(i)+'*')
	print('')