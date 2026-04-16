try:
    maximum_marks = int(input("Enter the maximum marks: "))
    print("Enter marks for the following subjects:")
    english = float(input("English: "))
    math = float(input("Math : "))
    science = float(input("Science: "))
    sst = float(input("Social studies: "))

    total = english + math + science + sst

    percentage = (total / (maximum_marks * 4)) * 100

    print(percentage, "%")

except ZeroDivisionError, ValueError:
    print("Wrong input")
