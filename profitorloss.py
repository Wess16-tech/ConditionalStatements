actual_amount = float(input("Enter the actual amount: "))
sale_amount = float(input("Enter the sales amount: "))

if(sale_amount > actual_amount):
    amount = sale_amount - actual_amount
    print("Profit: {0} ".format(amount))
else:
    print("no profit")