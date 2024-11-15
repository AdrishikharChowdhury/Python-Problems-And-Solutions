def factorial(num):
    if(num==1):
        return 1
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
number=int(input("Enter the number to find it's factorial: "))
fact=factorial(number)
print("The factorial of ",number," is ",fact)