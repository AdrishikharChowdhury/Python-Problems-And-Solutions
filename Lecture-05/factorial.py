n=int(input("Enter the number to find its factorial: "))
fact=1
if n==0:
    print("0 has no factorial")
elif n==1:
    print("factorial of 1 is 0")
else:
    for i in range(1,n+1):
        fact=fact*i
print("Factorial of ",n,"is ",fact)