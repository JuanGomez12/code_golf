for i in range(1,101):
	w=''
	if i%3==0:
		w+='Fizz'
	if i%5==0:
		w+='Buzz'
	if i%3 and i%5:
		w=i
	print(w)
