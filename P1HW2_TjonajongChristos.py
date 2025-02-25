# Christos Tjonajong
# 2/25/25
# P1HW2
# Calculcates travel expenses

#-----Pseudocode-----
# Tell what the program does
# Ask for budget, destination, cost of gas, cost of hotel, and cost of food
# Display the value of each prompt
# Add costs and subtract them from budget

print('This program calculates and displays travel expenses\n')
budget = int(input('Enter budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gasMoney = int(input('How much do you think you will spend on gas? '))
print()
hotelMoney = int(input('Approximately, how much will you need for accomodation/hotel? '))
print()
foodMoney = int(input('Last, how much do you need for food? '))
print()

print('------------Travel Expenses------------')
print('Location:', destination)
print('Intial Budget:', budget)
print()
print('Fuel:', gasMoney)
print('Accomodation:', hotelMoney)
print('Food:', foodMoney)
print()
print('Remaining Balance:', budget - (gasMoney + hotelMoney + foodMoney))
