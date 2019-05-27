p=list(map(int,input().split()))
a=p[1]
b=list(p[2::])
s=0
for i in range(0,a):
  s+=b[i]
print(s)
