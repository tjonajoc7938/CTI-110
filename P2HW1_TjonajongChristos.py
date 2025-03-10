# Christos Tjonajong
# 3/10/25
# P2HW1
# Calculcates travel expenses

#-----Pseudocode-----
# Tell what the program does
# Ask for budget, destination, cost of gas, cost of hotel, and cost of food
# Display the value of each prompt
# Add costs and subtract them from budget


print('This program calculates and displays travel expenses\n')
budget = float(input('Enter budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gasMoney = float(input('How much do you think you will spend on gas? '))
print()
hotelMoney = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
foodMoney = float(input('Last, how much do you need for food? '))
print()

print('------------Travel Expenses------------')
print(f'{"Location:":<19} {destination:<19}')
print(f'{"Initial Budget:":<19} ${budget:.2f}')
print(f'{"Fuel:":<19} ${gasMoney:.2f}')
print(f'{"Accomodation:":<19} ${hotelMoney:.2f}')
print(f'{"Food:":<19} ${foodMoney:.2f}')
print('---------------------------------------')
print()

print(f'{"Remaining Balance:":<19} ${(budget - (gasMoney + hotelMoney + foodMoney)):.2f}')
