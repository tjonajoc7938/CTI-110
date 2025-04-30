# Christos Tjonajong
# 4/7/25
# P4HW1
# Performs more advanced calculations on grades

grades = []

numScores = int(input("How many scores do you want to enter? "))

for score in range(1, (numScores + 1)):
    grade = int(input(f"Enter score #{score}: "))
    while grade < 0 or grade > 100:
        print("Invalid score entered!")
        print("Score should between 0 and 100")
        grade = int(input(f"Enter score #{score} again: "))
    grades.append(grade)

print('------------Results------------')
print(f'{"Lowest Grade":<15}: {min(grades)}')
grades.remove(min(grades))
print(f'{"Modified list":<15}: {grades}')
average = (sum(grades) / len(grades))
print(f'{"Average":<15}: {average:.2f}')
if average >= 90:
    print(f'{"Grade":<15}: A')
elif average >= 80:
    print(f'{"Grade":<15}: B')
elif average >= 70:
    print(f'{"Grade":<15}: C')
elif average >= 60:
    print(f'{"Grade":<15}: D')
else:
    print(f'{"Grade":<15}: F')
print('-------------------------------')
