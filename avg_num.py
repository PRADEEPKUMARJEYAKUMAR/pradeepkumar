a=int(input())
c=list(map(int,input().split()))
s=0
s1=0
while(s<len(c)):
  s1+=c[s]
  s+=1
p=s1//a
print(p)
  
  
