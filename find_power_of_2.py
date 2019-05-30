n=int(input())
for i in range(1,n):
    s=2**i
    if s==n:
        print("yes")
        break
else:
    print("no")
    
