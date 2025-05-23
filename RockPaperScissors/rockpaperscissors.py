import random

while True:
    r ='''Rock
            _______
        ---'   ____)
                (_____)
                (_____)
                (____)
        ---.__(___)
    '''

    p='''Paper
            _______
        ---'   ____)____
                    ______)
                    _______)
                _______)
        ---.__________)
    '''

    s='''Scissors
            _______
        ---'   ____)____
                    ______)
                __________)
                (____)
        ---.__(___)'''

    print("What do you choose? Type 1 for rock, 2 for paper and 3 for scissors")

    #user
    a=int(input())
    if(a==1):
        print(r)
    elif(a==2):
        print(p)
    elif(a==3):
        print(s)
    else:
        print("Wrong Input")


    #computer
    b= random.randint(1,3)
    if(b==1):
        print(r)
    elif(b==2):
        print(p)
    elif(b==3):
        print(s)


    #comparision
    if(a==b):
        print("Draw")
    elif(a==1 and b==3) or (a==2 and b==1) or (a==3 and b==2):
        print("You win")
    else:
        print("You lose")
    c=input("Do you want to play Again? Y or N: ").lower()
    if(c!="y"):
        print("Thank You!")
        break
