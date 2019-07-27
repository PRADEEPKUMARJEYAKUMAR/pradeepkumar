a=list(map(int,input().split()))
s=0
for i in a:
    s=s+int(i)
if(s%2==0):
    print("even")
else:
    print("odd")
