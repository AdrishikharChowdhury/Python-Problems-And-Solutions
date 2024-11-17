import random
def guesser(x,target):
    if x=="Quit":
       return False
    x=int(x)
    if x==target:
        print("You Won.You have guessed the correct number:\nAns: ",target)
        return False
    elif x<target:
        print("You have entered a small number.Guess bigger number: ")
    else:
        print("You have guessed big number.Guess smaller number: ")

def difficulty():
    print("Enter the game difficulty:")
    print("1.Easy\n2.Medium\n3.Hard\n4.Nightmare")
    while True:
        ch=int(input("Your choice: "))
        match(ch):
            case 1:
                print("Chosen Difficulty: Easy")
                print("No. of turns: ",15)
                return 1,50,14
            case 2:
                print("Chosen Difficulty: Medium")
                print("No. of turns: ",12)
                return 1,100,12
            case 3:
                print("Chosen Difficulty: Hard")
                print("No. of turns: ",10)
                return 1,500,10
            case 4:
                print("Chosen Difficulty: Nightmare")
                print("No. of turns: ",8)
                return 1,1000,8
            case _:
                print("Wrong Input!!!!Try Again")
n1,n2,turns=difficulty()
target=random.randint(n1,n2)
while turns!=0:
    x=input("Enter the number to guess or Quit: ")
    ip=guesser(x,target)
    if ip==False:
        break
    turns-=1
    print("Turn Left: ",turns)
if(turns==0):
    print("You lost.The number was:",target)
print("=====GAME OVER=====")