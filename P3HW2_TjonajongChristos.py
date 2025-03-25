# Christos Tjonajong
# 3/25/25
# P3HW2
# Displays employee pay information

# Pseudocode:
# Ask for employee information (name, hours, pay rate)
# Display employee name
# Columns for hours, pay rate, overtime, overtime pay, regular pay, and gross pay under
# Display the numbers for each column under the column name

name = input("Enter employee's name: ")
hours = int(input("Enter the number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

if hours > 40:
    overtime = hours - 40
    overtimePay = overtime * (1.5 * rate)
    regPay = (hours - overtime) * rate
else:
    overtime = 0
    overtimePay = 0
    regPay = hours * rate

gross = regPay + overtimePay

print("---------------------------------------")

print(f"Employee name:     {name}\n")
print("Hours Worked     "
      "Pay Rate     "
      "OverTime     "
      "OverTime Pay     "
      "RegHour Pay     "
      "Gross Pay     ")
print("------------------------------------------------------------------------------------------")
print(f"{hours:<17.1f}"
      f"{rate:<13.1f}"
      f"{overtime:<13.1f}"
      f"${overtimePay:<16.2f}"
      f"${regPay:<15.2f}"
      f"${gross:.2f}")
