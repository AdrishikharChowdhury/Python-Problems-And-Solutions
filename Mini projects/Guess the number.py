import random
def guesser(name,x,target):
    if x=="Quit":
       return False
    x=int(x)
    if x==target:
        print(name," won.You have guessed the correct number:","\nAns",target)
        return False
    elif x<target:
        print(name," you have entered a small number.Guess bigger number: ")
    else:
        print(name," you have guessed big number.Guess smaller number: ")

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
print("Choose your game mode:")
print("1.Single player\n2.Two player")
j=True
while j:
    j=False
    ch=int(input("Enter your choice: "))
    match ch:
        case 1:
            name1=input("Enter your name player: ")
            while turns!=0:
                x=input("Enter the number to guess or Quit: ")
                ip=guesser(name1,x,target)
                if ip==False:
                    break
                turns-=1
                print("Turn Left: ",turns)
            if(turns==0):
                print("You lost.The number was:",target)
        case 2:
            name1=input("Enter your name player 1: ")
            name2=input("Enter your name player 2: ")
            while turns!=0:
                x1=int(input(f"{name1} Enter the number to guess or Quit: "))
                x2=int(input(f"{name2} Enter the number to guess or Quit: "))
                ip1=guesser(name1,x1,target)
                ip2=guesser(name2,x2,target)
                if ip1==False:
                    print(name2," lost.Better Luck Next Time")
                    break
                if ip2==False:
                    print(name1," lost.Better luck next time")
                    break
                turns-=1
                print("Turn Left: ",turns)
            if(turns==0):
                print("Both of you lost.The number was:",target)
                print("Better Luck Next Time")
        case _:
            print("Sorry it is not available for multiplayer (Coming Soon...).")
            j=True
print("=====GAME OVER=====")