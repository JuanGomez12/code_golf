import sys
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for a in sys.argv[1:]:
    b=list(a[::-1])
    n=p=d[b.pop(0)]
    for v in b:
        k=d[v]
        n=n-k if p>k else n+k
        p=k
    print(n)