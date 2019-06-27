a=input()
l=[]
n=[]
for i in a:
    if str(i).isalpha():
        l.append(i)
    if str(i).isnumeric():
        n.append(i)
if(len(l)>0 and len(n)>0):
    print("Yes")
else:
    print("No")

