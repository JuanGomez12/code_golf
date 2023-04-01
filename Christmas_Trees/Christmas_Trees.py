r=range
p=print
[([p(' '*(i-j)+'*'*(2*j-1))for j in r(1,i)],p(' '*~-i+'*\n'))for i in r(4,11)]