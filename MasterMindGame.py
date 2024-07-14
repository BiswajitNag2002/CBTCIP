from getpass import getpass
print("\t\t\t\t\tWelcome!! MasterMind Game ....")
p1=input("Enter player1's name : ")
p2=input("Enter player2's name : ")
print(f'''Player1 -> {p1}\nPlayer2 -> {p2}\nGame started...''')
p1_no=getpass(prompt=f"{p1}, please Enter a 4 digit number : ")
p2_no=input(f"{p2}, Please guess a 4 digit number : ")
if p1_no == p2_no:
    print(f"{p2} You are MasterMind....")
else:
    j=0
    while True:
        j+=1
        s=""
        for i in range(4):
            if p1_no[i]==p2_no[i]:
                s+=p1_no[i]
            else:
                s+="X"
        if s != p1_no:
            print(f"{p1} generating the hint : {s}")
            p2_no=input(f"{p2} ,Now guess the 4 digit number once more : ")
        if s == p1_no :
            print(f"{p2} ,Now you guess the number correctly .. with {j} no of attempts")
            break
    
    p2_no=getpass(prompt=f"{p2}, Please Enter a 4 digit number whice {p1} gonna guess :")
    print(f"Now {p1} It is your turn to guess a 4 digit number...")
    p1_no=input(f"{p1}, Guess the 4 digit number : ")
    k=0
    while True:
        k+=1
        s=""
        for i in range(4):
            if p1_no[i]==p2_no[i]:
                s+=p1_no[i]
            else:
                s+="X"
        if s != p2_no:
            print(f"{p2} generating the hint : {s}")
            p1_no=input(f"{p1} ,Now guess the 4 digit number once more : ")
        if s == p2_no :
            print(f"{p1} ,Now you guess the number correctly .. with {k} no of attempts")
            break
    
    if k == j:
        print("Draw Match!!")
    elif k < j:
        print(f"{p1} You are MasterMind...")
    else:
        print(f"{p2} You are MasterMind...")
print(f"\nThank You {p1} & {p2} for playing MasterMind Game.....Please Come again !!")