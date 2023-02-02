def happy(nums):
	happy_set=[]
	nums = sum([int(num)**2 for num in str(nums)])
	while nums not in happy_set:
		happy_set+=[nums]
		nums = sum([int(num)**2 for num in str(nums)])
	return nums

for i in range(201):
	num = happy(i)
	if num==1:print(i)