# Chad Wiram
#3/12/2026
# P3HW2
# This program calculated an employees salary and to continue loop until done

# To calculate totals variables
total_employee = 0
total_overtime_pay = 0 
total_regular_pay = 0
total_gross_pay = 0
employee = ""

# Keep running so long as Employee name is not Done
while employee != "Done":
    print()
    employee = input(f"Enter employee's name or 'Done' to terminate: ")
    if employee.lower() == "done":
        break
    
    #Cotinue to get information if employee name is entered
    hours_worked = float(input(f"How many hours did {employee} work? "))
    pay_rate = float(input(f"What is {employee}'s pay rate? "))

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
    print()
    print(f"Employee name: {employee}")
    print()
    print(f"{'Hours Worked':<14} {'Pay Rate':<10} {'OverTime':<10} {'OverTime Pay':<15} {'Regular Pay':<14} {'Gross Pay'}")
    print('-' *80)

    print(f"{hours_worked:<14.2f} ${pay_rate:<9.2f} {overtime_hours:<10.2f} ${overtime_pay:<14.2f} ${regular_pay:<13.2f} ${gross_pay:.2f}")
    print()

    # Calculate totals based on entered information
    total_employee += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

#Print summary
print()
print(f"Total number of employees entered: {total_employee}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
print()



 
  


