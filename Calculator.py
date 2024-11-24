a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
print("Enter your operation:")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
ch=int(input("Enter your choice: "))
match ch:
    case 1:
        y=a+b
        print("Your output is ",y)
    case 2:
        y=a-b;
        print("Your output is ",y)
    case 3:
        y=a*b
        print("Your output is ",y)
    case 4:
        if b==0:
            print(f"You can't divide {a} with 0")
        else:
            y=a/b
            print("Your output is ",y)
    case 5:
        j=True
        print("Thank you for using our calculator")
    case _:
        print("Wrong Input Try Again")
    