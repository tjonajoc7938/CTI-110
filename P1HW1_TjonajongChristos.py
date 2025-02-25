# Christos Tjonajong
# 2/21/25
# P1HW1
# Performs basic mathematical expressions

print('-----Calculating Exponents----\n')
base = int(input('Enter an integer as the base value: '))
exponent = int(input('Enter an integer as the exponent: '))
print()
print(base, 'raised to the power of', exponent, 'is', base**exponent, '!!', '\n')

print('-----Addition and Subtraction----\n')
startInt = int(input('Enter a starting integer: '))
addInt = int(input('Enter an integer to add: '))
subInt = int(input('Enter an integer to subtract: '))
print()
print(startInt, '+', addInt, '-', subInt, 'is equal to', startInt+addInt-subInt)
