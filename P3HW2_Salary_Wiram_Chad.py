# Chad Wiram
#3/12/2026
# P3HW2
# This program calculated an employees salary

# Get employee information
print()
employee = input(f"Enter employee's name: ")
hours_worked = float(input(f"Enter number of hours worked: "))
pay_rate = float(input(f"Enter employee's pay rate: "))
print('-' *37)

# Calculate OverTime hours
if hours_worked > 40:
    overtime_hours = hours_worked - 40
else: 
    overtime_hours = 0 

# Calculate Regular hours
regular_hours = hours_worked - overtime_hours

#Calculate pay
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * pay_rate * 1.5
gross_pay = regular_pay + overtime_pay 

# Calculate data based off usesr input
print(f"Employee name: {employee}")
print()
print(f"{'Hours Worked':<14} {'Pay Rate':<10} {'OverTime':<10} {'OverTime Pay':<15} {'Regular Pay':<14} {'Gross Pay'}")
print('-' *80)

print(f"{hours_worked:<14.2f} ${pay_rate:<9.2f} {overtime_hours:<10.2f} ${overtime_pay:<14.2f} ${regular_pay:<13.2f} ${gross_pay:.2f}")
print()


