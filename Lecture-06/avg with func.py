def avg(num,n):
    sum=0
    for i in range(n):
        sum+=num[i]
    return float(sum/n)
num=[]
size=int(input("Enter the size of the array: "))
for i in range(size):
    num.append(float(input("Enter element: ")))
average=avg(num,size)
print("The average is: ",average)