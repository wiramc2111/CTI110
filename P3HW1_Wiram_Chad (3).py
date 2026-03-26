# Chad Wiram
#3/9/2026
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

# Get variable to get grade from user
print()
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
print()

grades = [mod1, mod2, mod3, mod4, mod5, mod6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

print("------------Results------------")
print(f"{'Lowest Grade:':<20}{low}")
print(f"{'Highest Grade:':<20}{high}")
print(f"{'Sum of Grades:':<20}{sum}")
print(f"{'Average:':<20}{avg:.2f}")
print('-' * 40)

# determine letter grade for average
if avg >= 90:
    print(f"Your grade is: A")

if avg > 80:
    if avg == 80:
        print(f"Your grade is: B")
    if avg <= 89:
        print(f"Your grade is: B")

if avg > 70:
    if avg == 70:
        print(f"Your grade is: C")
    if avg <= 79:
        print(f"Your grade is: C")
    
if avg >= 60:
    if avg == 60:
        print(f"Your grade is: D")
    if avg <= 69:
        print(f"Your grade is: D")

else:
    print("Your grade is: F")







