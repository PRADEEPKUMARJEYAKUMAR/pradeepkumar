n=input()
a=len(n)
n=int(n)
t=n
r=s=0
while n>0:
    r=n%10
    s=s+r**a
    n=n//10
if t==s:
    print("yes")
else:
    print("no")
