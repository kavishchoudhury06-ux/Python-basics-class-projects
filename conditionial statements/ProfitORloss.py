Making_cost = float(input("Enter the making cost: "))
Selling_price = float(input("Enter the selling price: "))

if Selling_price > Making_cost:
    print("It is a profit")
elif Selling_price < Making_cost:
    print("It is a loss")
else:
    print("It is not a profit nor a loss")