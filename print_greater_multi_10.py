a=input()
b=len(a)
if(b==1):
    print("10")
elif(b==2):
    p=a[0]
    c=a[1]
    p=int(p)+1
    print(str(p)+"0")
elif(b==3):
    p=a[0]
    c=a[1]
    q=a[2]
    if(int(c)==0 and int(q)==0):
        p=int(p)+1
        print(str(p)+"1"+"0")
    else:
        c=int(c)+1
        print(str(p)+str(c)+"0")
elif(b==4):
    p=a[0]
    c=a[1]
    q=a[2]
    d=a[3]
    if(int(c)==0 and int(q)==0 and int(d)==0):
        print(str(p)+"0"+"1"+"0")
    elif(int(q)==0 and int(d)==0):
        print(str(p)+str(c)+"1"+"0")
    else:
        q=int(q)+1
        print(str(p)+str(c)+str(q)+"0")
else:
    print("10000")
        
