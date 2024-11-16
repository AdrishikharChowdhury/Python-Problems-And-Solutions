import random
target=random.randint(1,100)
while True:
    x=input("Enter the number to guess or Quit: ")
    if x=="Quit":
        break
    x=int(x)
    if x==target:
        print("You have guessed the correct number:\nAns: ",x)
        break
    elif x<target:
        print("You have entered a small number.Guess bigger number: ")
    else:
        print("You have guessed big number.Guess smaller number: ")
print("=====GAME OVER=====")