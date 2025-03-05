# Christos Tjonajong
# 03/05/25
# P2LAB2
# Makes a dictionary to hold MPG for various vehicles

vehicles = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = vehicles.keys()

print(keys)
car = input('\nEnter a vehicle to see its mpg: ')
print(f'\nThe {car} gets {vehicles[car]} mpg.')

miles = int(input(f'\nHow many miles will you drive the {car}? '))
print(f'\n{(miles / vehicles[car]):.2f} gallon(s) of gas are needed to drive the {car} {float(miles)} miles.')
