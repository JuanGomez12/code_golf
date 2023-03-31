import sys
d={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL', 50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
for a in sys.argv[1:]:
 a=int(a)
 b=''
 while a>0:
  for k in sorted(list(d.keys()), reverse=True):
   while a>=k:
    b=b+d[k]
    a-=k
 print(b)