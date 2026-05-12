a = int(input("Enter your attendence"))
if a >= 75:
    print("You are eligible for the exam")
else:
    m = input("Do you have medical cause (y/n)")
    if m == "y":
        print("You are allowed for the exam")
    else:
        print("You are not allowed for the exam")