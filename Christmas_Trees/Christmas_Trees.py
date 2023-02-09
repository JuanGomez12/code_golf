r=range
p=print
for i in r(4,11):
	for j in r(1,i):
		p(' '*(i-j)+'*'*(2*j-1))
	p(' '*~-i+'*\n')