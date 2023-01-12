for i in range(1,1001):
	cs={2:'Foo', 3:'Fizz', 5:'Buzz', 7:'Bar'}
	w=''
	for c in cs:
		if i%c==0:
			w+=cs[c]
	if not w:
		w=i
	print(w)
