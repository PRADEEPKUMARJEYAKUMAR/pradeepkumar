def fob(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fob(a-1)+fob(a-2)
n=int(input())
for a in range(1,n+1):
    print(fob(a),end=" ")
