'''
10.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
'''

units=int(input("Enter the number of units: "))

actual_cost=units*100


if actual_cost>1000:
    total_cost=actual_cost-(0.1*actual_cost)
    print(f'Total cost= {total_cost}')
else:
    print(f'Total cost= {actual_cost}')