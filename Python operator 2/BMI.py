weight = float(input("Enter your weight in kilograms: "))
height = float(input("enter your height in centimeters: "))
height /= 100

bmi = weight / (height*height)
print(bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("normal")
elif bmi >= 25 and bmi <= 29.9:
    print("overweight")
elif bmi >= 30: 
    print("obese")

