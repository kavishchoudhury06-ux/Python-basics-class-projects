password = str(input("Enter a password: "))
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
num = "1234567890"
score = 0
for i in password:
    if i in lower:
        score = score+1 
        break
        
for i in password:
    if i in num:
        score = score+1 
        break
    
for i in password:
    if i in upper:
        score = score+1 
        break
    
if score == 3:
    print("Valid password")
else:
    print("Invalid password")

    
        
                
            
    
            

