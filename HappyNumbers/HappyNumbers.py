def h(n):
	s=[]
	while n not in s:
		s+=[n]
		n=sum([int(i)**2 for i in str(n)])
	return n
for i in range(201):
	if h(i)==1:print(i)