grade = int(input("Enter your grade from 1-10: "))

if grade >= 1 and grade <= 3:
    print("You are in begginer level")
elif grade >= 4 and grade <= 5:
    print("You are in intermediate level")
elif grade >= 6 and grade<= 8:
    print("You are in advanced level")
else:
    print("You are in expertise level")