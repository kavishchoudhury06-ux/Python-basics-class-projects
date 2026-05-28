def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

num1= int(input("Enter the first number to calculate: "))

num2 = int(input("Enter the second number to calculate: "))

operation = str(input("Enter the operation: (A, s, m, d): "))

operation = operation.lower()

if operation == "a":
    print(add(num1, num2))
elif operation == "s":
    print(sub(num1, num2))
    
elif operation == "m":
    print(mul(num1, num2))
    
elif operation == "d":
    print(div(num1, num2))
    
else:
    print("You havent selected valid operation")
    
    

