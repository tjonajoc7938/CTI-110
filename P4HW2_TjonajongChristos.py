# Christos Tjonajong
# 4/8/25
# P4HW2
# Displays employee pay information for multiple employees


totalOvertime = 0
totalReg = 0
totalGross = 0
numEmployees = 0
name = input("Enter employee's name or 'Done' to terminate: ")

while name != "Done":
    numEmployees += 1
    hours = int(input(f"How many hours did {name} work? "))
    rate = float(input(f"What is {name}'s pay rate? "))

    if hours > 40:
        overtime = hours - 40
        overtimePay = overtime * (1.5 * rate)
        regPay = (hours - overtime) * rate
        totalOvertime += overtimePay
    else:
        overtime = 0
        overtimePay = 0
        regPay = hours * rate

    gross = regPay + overtimePay
    totalReg += regPay
    totalGross += gross

    print("\n---------------------------------------")
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
    name = input("\nEnter employee's name or 'Done' to terminate: ")

print(f"\nTotal number of employees entered: {numEmployees}")
print(f"Total amount paid for overtime: ${totalOvertime}")
print(f"Total amount paid for regular hours: ${totalReg}")
print(f"Total amount pain in gross: ${totalGross}")
