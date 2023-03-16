import sys
num_dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
def r2a(nums):
    if len(nums)>1:
        n=0
        nums2=list(nums)
        while nums2:
            num=num_dict[nums2.pop(0)]
            if nums2 and num<num_dict[nums2[0]]:
                n+= num_dict[nums2.pop(0)] - num
            else:
                n+=num
        return n
    else:
        return num_dict[nums]
for arg in sys.argv[1:]:
    print(r2a(arg))