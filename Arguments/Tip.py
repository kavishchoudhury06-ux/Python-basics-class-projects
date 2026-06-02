def tip_percentage(bill_amount, tip_amount):
    if bill_amount<= 0:
        print("Bill amount must be greater than zero")
    else:
        percentage = (tip_amount/bill_amount)*100 
        return percentage
        
print(tip_percentage(354, 56))

