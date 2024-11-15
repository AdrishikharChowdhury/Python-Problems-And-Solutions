def odd_even(a):
    if(a%2!=0):
        return "ODD"
    else:
        return "Even"
n=int(input("Enter the no. to find if it's odd or even: "))
ans=odd_even(n)
print(ans)