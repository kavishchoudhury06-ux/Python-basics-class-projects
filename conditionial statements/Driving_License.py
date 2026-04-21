Age = float(input("Enter your age"))
if Age >= 18:
    DrL = str(input("You have lisence? (y/n)"))
    if DrL == "y":
        Valid = str(input("Driving lisence is valid? (y/n) "))
        if Valid == "y":
            print("Allowed")
        else:
            print("Not allowed")
    else: 
        print("Not allowed")   
else:
    print("Not allowed")   

