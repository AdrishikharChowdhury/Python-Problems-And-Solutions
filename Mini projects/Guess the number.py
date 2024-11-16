import random
def difficulty():
    print("Enter the game difficulty:")
    print("1.Easy\n2.Medium\n3.Hard\n4.Nightmare")
    while True:
        ch=int(input("Your choice: "))
        match(ch):
            case 1:
                print("Chosen Difficulty: Easy")
                return 1,50
            case 2:
                print("Chosen Difficulty: Medium")
                return 1,100
            case 3:
                print("Chosen Difficulty: Hard")
                return 1,500
            case 4:
                print("Chosen Difficulty: Nightmare")
                return 1,1000
            case _:
                print("Wrong Input!!!!Try Again")

n1,n2=difficulty()
target=random.randint(n1,n2)
while True:
    x=input("Enter the number to guess or Quit: ")
    if x=="Quit":
       break
    x=int(x)
    if x==target:
        print("You have guessed the correct number:\nAns: ",target)
        break
    elif x<target:
        print("You have entered a small number.Guess bigger number: ")
    else:
        print("You have guessed big number.Guess smaller number: ")
print("=====GAME OVER=====")