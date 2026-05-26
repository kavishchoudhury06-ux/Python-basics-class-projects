import random
num = random.randint(1, 50)
print(num)


win = "no"

i = 5

while i > 0:
    if win == "no":
        guess = int(input("Enter a guess: "))
        if guess == num:
            print("You got it right")
            win == "yes"
            break
        elif guess >= (num//4)*3:
            print("Hot")
            print(f"You have {i-1} attemts remaining")
            
        elif guess >= (num//4)*2:
            print("warm")
            print(f"You have {i-1} attemts remaining")
            
        elif guess >= (num//4):
            print("Cold")
            print(f"You have {i-1} attemts remaining")
        else:
            print("Ice Cold")
            print(f"You have {i-1} attemts remaining")
        i = i-1
    
else:
    print("The number was:", num)
        
    
    