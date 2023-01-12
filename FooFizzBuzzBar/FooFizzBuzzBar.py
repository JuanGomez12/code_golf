for i in range(1,1001):
	d={2:'Foo',3:'Fizz',5:'Buzz',7:'Bar'}
	w=''.join([d[c] for c in d if not i%c])
	if not w:
		w=i
	print(w)