vehicle = str(input("car or bike: "))
vehicle = vehicle.lower()
if vehicle == "car":
    print("You have selected car")
    CarType = str(input("Sedan or SUV: "))
    CarType = CarType.lower()
    if CarType == "sedan":
        print("You have selected sedan")
    elif CarType == "suv":
        print("You have selected SUV")
    else:
        print("You have not selected a valid car type")
elif  vehicle == "bike":
    print("You have selected bike")
    BikeType = str(input("scooter or bike: "))
    BikeType = BikeType.lower()
    if BikeType == "scooter":
        print("You have selected Scooter")
    elif BikeType == "bike":
        print("You have selected Bike")
    else:
        print("You have not selected a valid car type")
else:
    print("You have not selected a valid vehicle type")
    
    