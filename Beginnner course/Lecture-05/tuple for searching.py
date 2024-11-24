tuple=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the no. to search: "))
i=1
flag=0
for item in tuple:
    if item==x:
        print(x," is on position ",i)
        flag=1
    i+=1
if flag==0:
    print(x," is not in the tuple")