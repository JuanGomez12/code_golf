for i in range(1,1001):
	cs={2:'Foo',3:'Fizz',5:'Buzz',7:'Bar'}
	w=''.join([cs[c] for c in cs if not i%c])
	if not w:
		w=i
	print(w)