eng = int(input("Enter your marks for english"))
sst = int(input("Enter you marks f or social sudies"))
math = int(input("Enter your marks for mathematics"))
sci = int(input("Enter your marks fro science"))

total = eng + sst + math + sci
avg = total // 4

if avg >= 81 & avg <= 100:
    print("A grade")
elif avg >= 61 & avg <= 80:
    print("Grade B")
elif avg >= 41 & avg <= 60:
    print("Grade C")
else:
    print("Grade F")
