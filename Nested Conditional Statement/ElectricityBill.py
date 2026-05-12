units = int(input("Enter the units that you have consumed : "))

amount = 0

if units >= 0 and units <=50:

    amount = units * 5.74

elif units >= 51 and units <= 100:

    amount = (50 * 5.74) + ((units - 50) * 6.24)

elif units >= 101 and units <= 200:

    amount = (50 * 5.74) + (100 * 6.24) + ((units - 200) * 6.74)

elif units >= 201 and units <= 300:

    amount = (50 * 5.74) + (100 * 6.24) + (200 * 6.74) + ((units - 300) * 7.24)

elif units > 300:

    amount = (

(50 * 5.74)+ (100 * 6.24)+ (200 * 6.74) + (300 * 7.24) + ((units - 300) * 7.74) )

print(f"The total electricity bill is ₹{amount}")