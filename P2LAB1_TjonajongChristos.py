# Christos Tjonajong
# 03/05/25
# P2LAB1
# Calculates diamater, circumference, and area of a circle
import math
radius = float(input('What is the radius of the circle? '))

print(f'\nThe diameter of the circle is {(radius * 2):.1f}\n')
print(f'The circumference of the circle is {(2 * math.pi * radius):.2f}\n')
print(f'The area of the circle is {(math.pi * radius ** 2):.3f}\n')
