# Christos Tjonajong
# 3/13/25
# P2HW2
# Performs basic calculations of grades

# Pseudocode:
# Make a list to store grades
# Ask for the grades from each module
# Show the lowest grade
# Show the highest grade
# Show the sum of the grades
# Show the average

grades = []

grades.append(float(input('Enter grade for Module 1: ')))
grades.append(float(input('Enter grade for Module 2: ')))
grades.append(float(input('Enter grade for Module 3: ')))
grades.append(float(input('Enter grade for Module 4: ')))
grades.append(float(input('Enter grade for Module 5: ')))
grades.append(float(input('Enter grade for Module 6: ')))

print('------------Results------------')
print(f'{"Lowest Grade:":<19} {min(grades)}')
print(f'{"Highest Grade:":<19} {max(grades)}')
print(f'{"Sum of Grades:":<19} {sum(grades)}')
print(f'{"Average:":<19} {(sum(grades) / len(grades)):.2f}')
print('-------------------------------')

