a,b=list(map(int,input().split()))
for i in range(a,b):
    t=i
    c=len(str(i))
    s=0
    while t>0:
        r=t%10
        s+=r**c
        t//=10
    if i==s:
        print(i,end=' ')
