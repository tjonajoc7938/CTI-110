# Christos Tjonajong
# 4/10/25
# P4LAb2
# Displays multiplication table for integers

cont = 0

while cont != "no":
    integer = int(input("Enter an integer: "))
    print()
    while integer < 0:
        print("No negative numbers!")
        print()
        integer = int(input("Enter a integer >= 0: "))
        print()
    for number in range(1, 13):
        print(f"{integer} * {number} = {integer * number}")
    print()
    cont = input("Would you like to run the program again?: ")
    print()
print("Exiting program...")
