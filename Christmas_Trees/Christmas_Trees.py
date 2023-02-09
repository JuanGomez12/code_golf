r=range
p=print
for i in r(4,11):
	[p(' '*(i-j)+'*'*(2*j-1))for j in r(1,i)]
	p(' '*~-i+'*\n')