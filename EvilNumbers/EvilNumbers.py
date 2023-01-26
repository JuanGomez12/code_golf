for i in range(50):
	b=f'{i:>08b}'.count('1')
	if not b%2: print(i)