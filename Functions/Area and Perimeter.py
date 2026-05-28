def area(a, b):
    return(a*b)
def perimeter(a, b):
    return(2*(a+b))

length = int(input("Enter the length of the rectangle in centimeters: "))
breadth = int(input("Enter the breadth of the rectangle in centimeters: "))
print("The area is:", area(length, breadth), "square centimeters")
print("The perimeter is:", perimeter(length, breadth), "centimeters")
