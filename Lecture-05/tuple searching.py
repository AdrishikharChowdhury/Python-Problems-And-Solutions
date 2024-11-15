tuple=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the no. to search: "))
i=1
flag=0
while i<=len(tuple)-1:
    if tuple[i]==x:
        print(x," is on position ",i+1)
        flag=1
    i+=1
if flag==0:
    print(x," is not in the tuple")