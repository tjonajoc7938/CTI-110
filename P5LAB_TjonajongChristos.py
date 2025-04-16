# Christos Tjonajong
# 4/15/25
# P5LAB
# Simulates self-checkout giving change

import random


def disperse_change(payment):
    money = 100 * payment

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


def checkout():
    cost = round(random.uniform(0.01, 100.0), 2)
    print(f"You owe ${cost}")
    cash = float(input("How much cash will you put in the self-checkout? "))
    change = cash - cost
    print(f"Change is: ${change:.2f}\n")
    disperse_change(change)


checkout()
