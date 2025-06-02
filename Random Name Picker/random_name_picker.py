import random

while True:

    a=input("Enter names separated by spaces: ").split()
    print(random.choice(a))


    b=input("Do you want to choose again? Yes or No: ").capitalize()
    if b != "Yes":
        print("Thank You!")
        break
