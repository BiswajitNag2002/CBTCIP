import random #Importing external module named random

while True:
    computer_choice=random.randint(1,3) #Generating the computer choice

    #Generating computer choice as Stone / Paper / Scissor
    if computer_choice == 1:
        computer_choice="rock"
    elif computer_choice == 2:
        computer_choice="paper"
    else:
        computer_choice="scissor"

    user_choice = input("Enter your choice (rock / Paper / Scissor) -> ") #Taking User choice
    user_choice=user_choice.lower().strip()
    s=f'''Computer -> {computer_choice}\nYou      -> {user_choice}\n'''
    #comparing choices
    if computer_choice == user_choice:
        print(s)
        print("Match Draw !!")
    elif computer_choice == "rock":
        if user_choice == "paper":
            print(s)
            print("You Win")
        else:
            print(s)
            print("You loose. Better luck next time..")
    elif computer_choice == "paper":
        if user_choice == "rock":
            print(s)
            print("You loose. Better luck next time..")
        else:
            print(s)
            print("You Win")
    else:
        if user_choice == "rock":
            print(s)
            print("You Win")
        else:
            print(s)
            print("You loose. Better luck next time..")
    data=input("Do you wanna play once more ? (Yes / No) -> ")
    if data.lower() == "no":
        print("\nThank you for playing with me!! Come again..")
        break