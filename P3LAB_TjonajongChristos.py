# Christos Tjonajong
# 3/19/25
# P3LAB
# Calculates efficient amount of change

# -----Pseudocode-----
# Convert input to cents
# Divide with // and subtract from input
# Repeat until left with pennies

money = 100 * float(input('Enter the amount of money as a float: $'))

if money >= 100:
    dollars = int(money) // 100
    money -= dollars * 100
    if dollars > 1:
        print(f'{dollars} Dollars')
    else:
        print(f'{dollars} Dollar')
if money >= 25:
    quarters = int(money) // 25
    money -= quarters * 25
    if quarters > 1:
        print(f'{quarters} Quarters')
    else:
        print(f'{quarters} Quarter')
if money >= 10:
    dimes = int(money) // 10
    money -= dimes * 10
    if dimes > 1:
        print(f'{dimes} Dimes')
    else:
        print(f'{dimes} Dime')
if money >= 5:
    nickels = int(money) // 5
    money -= nickels * 5
    if nickels > 1:
        print(f'{nickels} Nickels')
    else:
        print(f'{nickels} Nickel')
if money >= 1:
    pennies = int(money) // 1
    money -= pennies
    if pennies > 1:
        print(f'{pennies} Pennies')
    else:
        print(f'{pennies} Penny')
else:
    print('No change')
