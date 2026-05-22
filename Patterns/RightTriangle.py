n = int(input("Enter a number: "))


for x in range(2, n+2):
    for y in range(1, x):
        print("*", end= " ")
    print()