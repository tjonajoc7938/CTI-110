# Christos Tjonajong
# 2/21/25
# P1HW1
# Performs basic mathematical expressions

print('-----Calculating Exponents----\n')
print('Enter an integer as the base value:')
base = int(input())
print('Enter an integer as the exponent:')
exponent = int(input())
print()
print(base, 'raised to the power of', exponent, 'is', base**exponent, '!!', '\n')
print('-----Addition and Subtraction----\n')
print('Enter a starting integer:')
startInt = int(input())
print('Enter an integer to add:')
addInt = int(input())
print('Enter an integer to subtract:')
subInt = int(input())
print()
print(startInt, '+', addInt, '-', subInt, 'is equal to', startInt+addInt-subInt)
