import sys
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def r(a):
    if len(a)>1:
        n=0
        b=list(a)
        while b:
            m=d[b.pop(0)]
            if b and m<d[b[0]]:
                n+=d[b.pop(0)]-m
            else:
                n+=m
        return n
    else:
        return d[a]
for arg in sys.argv[1:]:
    print(r(arg))