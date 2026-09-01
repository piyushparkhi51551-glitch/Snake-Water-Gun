import random
yourDict={"s":1, "w":-1,"g":0}
computer= random.choice([-1,0,1])
yourstr=input("Enter your Luck:").lower()

reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you=yourDict[yourstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if(computer==you):
    print("IT'S Draw")

else:
    if(computer ==-1 and you ==1):
        print("you win")

    elif(computer ==-1 and you ==0):
        print("you lose")

    elif(computer ==1 and you ==-1):
        print("you lose!")
            
    elif(computer ==1 and you ==0):
        print("you win!")

    elif(computer ==0 and you ==-1):
        print("you win!")

    elif(computer ==0 and you ==1):
        print("you lose!")

    else:
        print("something went wrong!")            