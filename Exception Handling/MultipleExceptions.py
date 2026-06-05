try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another smaller number"))
    if num1>num2:
        print(num1/num2)
    elif num2 > num1:
        raise IOError
except ValueError as ex:
    print("Only numbers are allowed")
    print(ex)
except ZeroDivisionError as ex:
    print("Division by zero is not allowed")
    print(ex)
except IOError:
    print("Write a number greater than first number")
    
else:
    print("There is no error")
finally:
    print("The exceptions are over")
