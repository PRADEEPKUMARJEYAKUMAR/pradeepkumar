p=list(map(int,input().split()))
s=0
for i in p:
    s=s-i
if(s%2==0):
    print("even")
else:
    print("odd")
