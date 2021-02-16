#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.



amount=float(input('enter the total amount : '))

if amount > 1000:
    print(amount,'Discount the amount of 10% ')
    discount=amount*0.1
    print(discount)
else:
    print(amount,'no discount')