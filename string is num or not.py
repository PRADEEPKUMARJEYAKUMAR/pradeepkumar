n=input()
l=['1','2','3','4','5','6','7','8','9','0','.']
for i in n:
    if i not in l:
        print("no")
        break
else:
    print("yes")
