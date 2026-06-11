import random

UserScore = 0
ComputerScore = 0


try:
    maxscore = int(input("Enter the ammount of points required to win "))
    print(f"Playing best of {maxscore}")
        
except ValueError:
    print("Invalid input")
    maxscore = int(input("Enter the ammount of points required to win "))
    print(f"Playing best of {maxscore}")
        


options = ["rock" , "paper" , "scissor"]
while True:
    UserChoice = input("Enter a choice: rock, paper, or scissor or q to quit: ").lower()
    ComputerChoice = random.choice(options)
    
    if UserChoice == "q":
        print(f"Score is {UserScore}-{ComputerScore}")
        if UserScore > ComputerScore:
            print("You win!!")
        elif ComputerScore > UserScore:
            print("You lose!!")
        break
        
    elif UserChoice not in options:
        print("Invalid input")
        continue
    
    print("Computer chose: ", ComputerChoice)
    
    
    if((UserChoice == "rock" and ComputerChoice == "scissors")
         or (UserChoice == "paper" and ComputerChoice == "rock")
         or (UserChoice == "scissor" and ComputerChoice == "paper" )
        ):
        UserScore += 1
        print(f"Score is {UserScore}-{ComputerScore}")
        if UserScore == maxscore:
            print("You win!!")
            break
        
    elif UserChoice == ComputerChoice:
        print("It is a tie!!")
        print(f"Score is {UserScore}-{ComputerScore}")
    
        
    else: 
        ComputerScore += 1
        print(f"Score is {UserScore}-{ComputerScore}")
        if ComputerScore == maxscore:
            print("Computer wins!!")
            break
        
        
    
    