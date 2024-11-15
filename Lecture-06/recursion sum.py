def sum_of_natural(n):
    if n==0:
        return 0
    return sum_of_natural(n-1)+n
a=int(input("Enter the limit of sum: "))
ans=sum_of_natural(a)
print("The sum of natural no. is ",ans)