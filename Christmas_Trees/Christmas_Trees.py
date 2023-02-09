r=range
p=print
for i in r(3,10):
	[p(' '*(i-j+1)+'*'*(2*j-1)) for j in r(1,i+1)]
	p(' '*(i)+'*\n')