def mergesort(n):
    if(len(n)>1):
        m=len(n)//2
        L=n[:m]
        R=n[m::]
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]< R[j]:
                n[k]=L[i]
                i+=1
            else:
                n[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            n[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            n[k]=R[j]
            j+=1
            k+=1
def printlist(n):
    for i in n:
        print(i,end=' ')
    print()
n=list(map(int,input().split()))
mergesort(n)
printlist(n)

